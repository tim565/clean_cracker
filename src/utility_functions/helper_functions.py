from src.configurations import SUPPORTED_ALGORITHMS_LENGTH_MAPPING


def get_hash_type(hash_to_test: str) -> str:
    """
    Determines the type of hash algorithm used based on the length of the hash.

    Parameters:
    hash_to_test (str): The hash to be tested.

    Returns:
    str: The type of hash algorithm used. If the hash length is not recognized, returns "Unknown Hash Type".
    """

    # Calculate the length of the hash
    hash_length = len(hash_to_test)

    # Check if the hash length is in the dictionary
    if hash_length in SUPPORTED_ALGORITHMS_LENGTH_MAPPING:
        return SUPPORTED_ALGORITHMS_LENGTH_MAPPING[hash_length]
    else:
        return 'Unknown Hash Type'


def get_hash_types_from_set(hash_set: set[str]) -> list[str]:
    found_hash_types = set()

    for hash_value in hash_set:
        hash_type = get_hash_type(hash_value)

        unknown_hash_type = hash_type == 'Unknown Hash Type'
        not_in_found_hash_types = hash_type not in found_hash_types

        if unknown_hash_type:
            return []

        elif not_in_found_hash_types:
            found_hash_types.add(hash_type)

    return list(found_hash_types)


def process_user_input(user_input: str) -> str:
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
