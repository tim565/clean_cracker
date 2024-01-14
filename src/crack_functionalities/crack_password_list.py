from src.file_functionalities.csv_operations import (read_csv_create_dictionary_list,
                                                     extract_column_of_former_csv_to_set)


def get_password_hashes_to_crack_from_csv(target_file_path, column_name_password_hashes):
    try:
        # Load hashes from user-given csv file; list of dicts containing password hashes and optionally more
        # columns such as usernames
        full_target_file = read_csv_create_dictionary_list(target_file_path)
        # Store hashes in set for higher efficiency
        hashes_to_crack_set = extract_column_of_former_csv_to_set(full_target_file, column_name_password_hashes)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:  # Generated in case column is not found in given csv file
        print(f"{ae}")
    else:
        # Set is required for cracking, list to later inform user about cracked passwords in the original file format
        return hashes_to_crack_set, full_target_file


def get_password_hashes_from_rainbow_table(rainbow_table_file_path, type_of_hash):
    try:
        full_rainbow_table = read_csv_create_dictionary_list(rainbow_table_file_path)
        # Store hashes in set for higher efficiency
        rainbow_table_hash_set = extract_column_of_former_csv_to_set(full_rainbow_table, type_of_hash)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:  # Generated in case column is not found in given csv file
        print(f"{ae}")
    else:
        # Set is required for cracking, full rainbow table to later derive plaintext passwords belonging to found hashes
        return rainbow_table_hash_set, full_rainbow_table
