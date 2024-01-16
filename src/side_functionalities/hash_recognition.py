import hashlib


def get_hash_type(hash_to_test):
    """
    Determines the type of hash algorithm used based on the length of the hash.

    Parameters:
    hash_to_test (str): The hash to be tested.

    Returns:
    str: The type of hash algorithm used. If the hash length is not recognized, returns "Unknown Hash Type".
    """

    # Dictionary mapping hash lengths to corresponding algorithms
    hash_algorithms = {
        32: "md5",
        40: "sha1",
        56: "sha224",
        64: "sha256",
        96: "sha384",
        128: "sha512"
    }

    # Calculate the length of the hash
    hash_length = len(hash_to_test)

    # Check if the hash length is in the dictionary
    if hash_length in hash_algorithms:
        return hash_algorithms[hash_length]
    else:
        return "Unknown Hash Type"
