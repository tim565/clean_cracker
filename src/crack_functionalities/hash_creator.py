import hashlib


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
