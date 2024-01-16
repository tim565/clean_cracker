from src.file_functionalities.csv_operations import read_csv_create_dictionary_list, \
    extract_column_of_former_csv_to_set, write_dicts_to_csv
from src.crack_functionalities.hash_cracker import find_intersection

current_type_of_hash = "sha256"


def get_password_hashes_and_list_of_dictionaries(file_path):
    """
    Reads a CSV file and creates a list of dictionaries representing the file contents.
    Extracts a specific column from the CSV file and stores the values in a set.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        tuple: A tuple containing the set of hashes and the list of dictionaries representing the file contents.
    """
    try:
        # Can be complete rainbow table or user-given target file
        full_list_of_dictionaries = read_csv_create_dictionary_list(file_path)
        # Store hashes in set for higher efficiency
        hash_set = extract_column_of_former_csv_to_set(full_list_of_dictionaries, current_type_of_hash)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:  # Generated in case column is not found in given csv file
        print(f"{ae}")
    else:
        # Set is required for cracking, full list of dicts is required for later assignments of hashes
        return hash_set, full_list_of_dictionaries


def find_plaintext_passwords_of_hashes(hashes_to_crack_set, hashes_rainbow_table, full_rainbow_table, type_of_hash):
    """
    Finds the plaintext passwords corresponding to a set of hashes by comparing them with a rainbow table.
    
    Args:
        hashes_to_crack_set (set): The set of hashes to crack.
        hashes_rainbow_table (set): The set of hashes from the rainbow table.
        full_rainbow_table (list): The complete rainbow table as a list of dictionaries.
        type_of_hash (str): The type of hash being used.
        
    Returns:
        list: A list of dictionaries containing the found hashes with their corresponding plaintext passwords.
    """
    # Compare the hashes of the rainbow table and the user-given hashes
    intersection_of_hashes = find_intersection(hashes_to_crack_set, hashes_rainbow_table)

    # List to store hashes from intersection with their plaintext passwords; list of dictionaries
    found_hashes_with_plaintext_passwords = []

    # Iterate through rainbow table to get plaintext passwords to found hashes
    for rainbow_element in full_rainbow_table:
        rainbow_hash = rainbow_element.get(type_of_hash)
        rainbow_password = rainbow_element.get('password')

        # Check if rainbow hashes part of intersection; if yes, append hash and plaintext password to list
        rainbow_hash_part_of_intersection = rainbow_hash in intersection_of_hashes
        if rainbow_hash_part_of_intersection:
            found_hashes_with_plaintext_passwords.append({'password': rainbow_password, 'hash': rainbow_hash})

    return found_hashes_with_plaintext_passwords


def add_plaintext_passwords_to_original_csv(full_target_file, found_hashes_with_plaintext_passwords, type_of_hash):
    """
    Adds the plaintext passwords to the original target file based on the found hashes.
    
    Args:
        full_target_file (list): The complete target file as a list of dictionaries.
        found_hashes_with_plaintext_passwords (list): The list of dictionaries containing the found hashes with their plaintext passwords.
        type_of_hash (str): The type of hash being used.
        
    Returns:
        list: The updated target file with the additional column for cracked plaintext passwords.
    """
    # Iterate through each element in original target file
    for target_element in full_target_file:
        target_password_hash = target_element.get(type_of_hash)

        # Iterate through hashes that are available as plaintext passwords
        for found_hash in found_hashes_with_plaintext_passwords:
            hash_available_as_plaintext = found_hash["hash"] == target_password_hash
            if hash_available_as_plaintext:
                # Add plaintext passwords with additional key in dictionary, later it is an additional csv column
                plaintext_password = found_hash.get('password')
                target_element['cracked_password'] = plaintext_password

    return full_target_file


def crack_password_list(rainbow_table_file_path, target_file_path, type_of_hash):
    """
    Cracks the passwords in the target file using a rainbow table.
    
    Args:
        rainbow_table_file_path (str): The path to the rainbow table file.
        target_file_path (str): The path to the target file.
        type_of_hash (str): The type of hash being used.
    """
    # Get set of hashes from rainbow table and complete rainbow table incl. plaintext passwords
    rainbow_table_hash_set, rainbow_table_complete = (
        get_password_hashes_and_list_of_dictionaries(rainbow_table_file_path))

    # Get set of hashes from target file and complete target file incl. columns such as username, email
    target_hash_set, target_file_complete = get_password_hashes_and_list_of_dictionaries(target_file_path)

    # Gain the intersection of both hash sets and assign plaintext password to each hash in intersection
    found_hashes_with_plaintext_passwords = (
        find_plaintext_passwords_of_hashes(target_hash_set, rainbow_table_hash_set, rainbow_table_complete,
                                           type_of_hash))

    # Add the plaintext passwords from intersection to according rows in original file
    full_target_file = add_plaintext_passwords_to_original_csv(target_file_complete,
                                                               found_hashes_with_plaintext_passwords, type_of_hash)

    # Write original file with new column cracked plaintext passwords to new csv file
    write_dicts_to_csv(full_target_file, "target_file_with_cracked_passwords.csv")
