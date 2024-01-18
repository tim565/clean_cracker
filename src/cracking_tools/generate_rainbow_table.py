import copy
from src.configurations import SUPPORTED_ALGORITHMS
from src.cracking_tools.hash_creator import hash_list
from src.utility_functions.csv_operations import read_csv_create_list, write_dicts_to_csv


def list_to_list_of_dicts(two_dimensional_list, keys):
    """
    Transposes a two-dimensional list and converts it into a list of dictionaries.
    
    Args:
        two_dimensional_list (list): The two-dimensional list to be transposed.
        keys (list): The keys to be used for creating dictionaries.
        
    Returns:
        list: A list of dictionaries where each dictionary represents a row of the transposed list.
    """
    result_list_of_dicts = []

    # Transpose the two-dimensional list
    transposed_list = list(map(list, zip(*two_dimensional_list)))

    for values in transposed_list:
        result_dict = dict(zip(keys, values))
        result_list_of_dicts.append(result_dict)

    return result_list_of_dicts


def get_cleartext_password_list(password_file_path, password_column_name="password"):
    """
    Reads a CSV file and extracts the cleartext passwords from the specified column.
    
    Args:
        password_file_path (str): The path to the CSV file.
        password_column_name (str, optional): The name of the column containing the passwords. Defaults to "password".
        
    Returns:
        list: A list of cleartext passwords extracted from the CSV file.
    """
    try:
        cleartext_password_list = read_csv_create_list(password_file_path, password_column_name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:
        print(f"{ae}")
    else:
        return cleartext_password_list


def generate_table_with_hashes(cleartext_password_list, user_given_hash_algorithms_list=SUPPORTED_ALGORITHMS):
    """
    Generates a table of hashed passwords using the specified hash algorithms.
    
    Args:
        cleartext_password_list (list): A list of cleartext passwords.
        user_given_hash_algorithms_list (list, optional): A list of hash algorithms to be used for hashing. 
            Defaults to SUPPORTED_ALGORITHMS.
            
    Returns:
        list: A list of dictionaries representing the table of hashed passwords, where each dictionary 
            corresponds to a row in the table.
    """
    # The hashed lists are stored here, e.g. a list for sha1, a list for sha256, a list for sha512
    hashed_lists = [cleartext_password_list]
    
    # The cleartext password list is hashed using the algorithms specified by the user.
    # If the user did not specify, all algorithms supported by this program are applied on the cleartext passwords.
    for hash_algorithm in user_given_hash_algorithms_list:
        hashed_list = hash_list(cleartext_password_list, hash_algorithm)
        hashed_lists.append(hashed_list)

    dictionary_keys = copy.deepcopy(user_given_hash_algorithms_list)
    dictionary_keys.insert(0, "cleartext password")

    print('len(hashed_lists): ', len(hashed_lists))
    # Use zip to pair corresponding elements from the three lists
    combined_list_of_dicts = list_to_list_of_dicts(hashed_lists, user_given_hash_algorithms_list)
    return combined_list_of_dicts


def generate_rainbow_table(password_list_file_path):
    """
    Generates a rainbow table by reading a password list file, hashing the passwords, and writing the results to a CSV file.
    
    Args:
        password_list_file_path (str): The path to the password list file.
        rainbow_table_name (str): The name of the rainbow table to be generated.
    """
    cleartext_password_list = get_cleartext_password_list(password_list_file_path, password_column_name="password")
    print('cleartext_password_list: ', cleartext_password_list)
    combined_list_of_dicts = generate_table_with_hashes(cleartext_password_list)
    write_dicts_to_csv(combined_list_of_dicts, "workspace/output/generated_rainbow_table.csv")
