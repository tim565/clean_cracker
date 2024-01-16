
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
