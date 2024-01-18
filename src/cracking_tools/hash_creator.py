import hashlib
from src.configurations import SUPPORTED_ALGORITHMS


def hash_list(input_values: list[str], hash_algorithm: str = 'sha256') -> list[str]:
    """
    Hashes a list of values (which are usually passwords) using the specified hash algorithm.

    Parameters:
    - input_values (list): List of values to be hashed.
    - hash_algorithm (str): Hash algorithm to use ('md5', 'sha1', 'sha224', 'sha256', 'sha384', or 'sha512').
      Default is 'sha256'.

    Returns:
    - list: List of hashed values corresponding to the input values.
    """
    hashed_values = []

    # Hash each value in list using function hash_string()
    for value in input_values:
        hashed_values.append(hash_string(value, hash_algorithm))

    return hashed_values


def hash_string(input_string: str, hash_algorithm: str) -> str:
    """
    Hashes an input string using the specified hash algorithm.

    Parameters:
    - input_string (str): The string to be hashed.
    - hash_algorithm (str): The hash algorithm to use. Supported values are
                            'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'.

    Returns:
    - str: The hexadecimal hash of the input string.
    """

    hash_libraries = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512
    }

    # Check if the specified algorithm is supported
    if hash_algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")

    # Create a hash object and update it with the bytes of the input string
    hash_obj = hash_libraries[hash_algorithm]()
    hash_obj.update(input_string.encode())
    hexadecimal_representation = hash_obj.hexdigest()

    return hexadecimal_representation
