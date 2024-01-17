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


def get_hash_types_from_set(hash_set):
    found_hash_types = set()
    for hash in hash_set:
        hash_type = get_hash_type(hash)
        if hash_type=="Unknown Hash Type":
            return []
        elif hash_type not in found_hash_types:
            found_hash_types.add(hash_type)
    return list(found_hash_types)


def process_user_input(user_input):
    """
    The user inputs the hash that should be used.
    The input can be in various formats such as Sha-256, SHA-256, sha 256, etc.
    This function standardizes the inputs by removing spaces, hyphens and converting letters to lowercase.
    """
    # Convert to lowercase
    processed_input = user_input.lower()

    # Remove spaces
    processed_input = processed_input.replace(" ", "")

    # Remove hyphens
    processed_input = processed_input.replace("-", "")

    return processed_input
