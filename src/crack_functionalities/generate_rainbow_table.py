from src.configurations import SUPPORTED_ALGORITHMS
from src.crack_functionalities.hash_creator import hash_values
from src.file_functionalities.csv_operations import read_csv_create_list, write_dicts_to_csv


def list_to_list_of_dicts(two_dimensional_list, keys):
    result_list_of_dicts = []

    # Transpose the two-dimensional list
    transposed_list = list(map(list, zip(*two_dimensional_list)))

    for values in transposed_list:
        result_dict = dict(zip(keys, values))
        result_list_of_dicts.append(result_dict)

    return result_list_of_dicts


def get_cleartext_password_list(password_file_path, password_column_name="password"):
    # This function processes inputs given by the user.
    # First it is verified if the given file is available and if the column supposed to be hashed is
    # contained in that file.
    # In case everything is ok, the cleartext passwords are extracted as a list from the user given file.
    try:
        cleartext_password_list = read_csv_create_list(password_file_path, password_column_name)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except AssertionError as ae:
        print(f"{ae}")
    else:
        return cleartext_password_list


def generate_table_with_hashes(cleartext_password_list, user_given_hash_algorithms_list=SUPPORTED_ALGORITHMS):
    # The hashed lists are stored here, e.g. a list for sha1, a list for sha256, a list for sha512
    hashed_lists = [cleartext_password_list]
    # The cleartext password list is hashed using the algorithms specified by the user.
    # If the user did not specify, all algorithms supported by this program are applied on the cleartext passwords.
    for hash_algorithm in user_given_hash_algorithms_list:
        hashed_list = hash_values(cleartext_password_list, hash_algorithm)
        hashed_lists.append(hashed_list)

    dictionary_keys = user_given_hash_algorithms_list
    dictionary_keys.insert(0, "cleartext_password")

    # Use zip to pair corresponding elements from the three lists
    combined_list_of_dicts = list_to_list_of_dicts(hashed_lists, user_given_hash_algorithms_list)
    return combined_list_of_dicts


def generate_rainbow_table(password_list_file_path, rainbow_table_name):
    cleartext_password_list = get_cleartext_password_list(password_list_file_path, password_column_name="password")
    combined_list_of_dicts = generate_table_with_hashes(cleartext_password_list)
    write_dicts_to_csv(combined_list_of_dicts, f"{rainbow_table_name}.csv")
