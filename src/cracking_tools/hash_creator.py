import hashlib

# TODO: Determine the difference between both functions and check whether they are actually necessary

def hash_values(input_values, hash_algorithm='sha256'):
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

    for value in input_values:
        # Create a new hash object using the specified algorithm
        hash_obj = hashlib.new(hash_algorithm)

        # Update the hash object with the password bytes
        hash_obj.update(value.encode('utf-8'))

        # Get the hexadecimal representation of the hashed password
        hashed_value = hash_obj.hexdigest()
        hashed_values.append(hashed_value)

    return hashed_values


def hash_string(input_string, hash_algorithm):
    """
    Hashes an input string using the specified hash algorithm.

    Parameters:
    - input_string (str): The string to be hashed.
    - hash_algorithm (str): The hash algorithm to use. Supported values are
                            'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'.

    Returns:
    - str: The hexadecimal hash of the input string.
    """

    supported_algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha224': hashlib.sha224,
        'sha256': hashlib.sha256,
        'sha384': hashlib.sha384,
        'sha512': hashlib.sha512
    }

    # Check if the specified algorithm is supported
    if hash_algorithm not in supported_algorithms:
        raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")

    # Create a hash object and update the it with the bytes of the input string
    hash_obj = supported_algorithms[hash_algorithm]()
    hash_obj.update(input_string.encode())
    hexadecimal_representation = hash_obj.hexdigest()

    return hexadecimal_representation
