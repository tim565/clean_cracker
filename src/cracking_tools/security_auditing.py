from src.cracking_tools.hash_cracker import find_intersection
from src.utility_functions.csv_operations import read_csv_create_dictionary_list, read_csv_create_list, \
    extract_column_of_former_csv_to_set, write_dicts_to_csv


def get_values_from_db_dump_file(file_path):
    try:
        # Complete rainbow table is extracted
        full_list_of_dictionaries = read_csv_create_dictionary_list(file_path)
        # Store hashes in set for higher efficiency
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:  # Generated in case column is not found in given csv file
        print(f"{ae}")
    else:
        # Set is required for cracking, full list of dicts is required for later assignments of hashes
        return full_list_of_dictionaries


def get_most_common_passwords(file_path, password_column_name="password"):
    """
    Reads a CSV file and extracts the cleartext passwords from the specified column.

    Args:
        file_path (str): The path to the CSV file.
        password_column_name (str, optional): The name of the column containing the passwords. Defaults to "password".

    Returns:
        list: A list of cleartext passwords extracted from the CSV file.
    """
    try:
        cleartext_password_list = read_csv_create_list(file_path, password_column_name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:
        print(f"{ae}")
    else:
        return set(cleartext_password_list)


def assign_found_hashes_to_db_dump(hash_intersection: set, db_dump: list):
    for i in db_dump:
        item_to_check = i["sha256"]
        weak_password = item_to_check in hash_intersection
        if weak_password:
            i["password_strength"] = "weak"
        else:
            i["password_strength"] = "strong"
    return db_dump


def audit_database_dump(db_dump_file_path: str, password_list_file_path: str):

    db_dump = get_values_from_db_dump_file(db_dump_file_path)

    most_common_passwords = get_most_common_passwords(password_list_file_path)

    db_hashes_set = extract_column_of_former_csv_to_set(db_dump, "sha256")

    intersection = find_intersection(db_hashes_set, most_common_passwords)

    db_dump_new = assign_found_hashes_to_db_dump(intersection, db_dump)

    write_dicts_to_csv(db_dump_new, "output_sec_audit.csv")
