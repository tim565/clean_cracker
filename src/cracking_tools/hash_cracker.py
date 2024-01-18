
def find_intersection(cracking_set: set, rainbow_set: set) -> set:
    """
    Finds the intersection of two sets. This is an efficient step to find hashes to crack contained in the rainbow table.

    Parameters:
    - cracking_set (set): The set of hashes that is supposed to be cracked.
    - rainbow_set (set): The set of hashes contained in the rainbow table.

    Returns:
    - intersection_set: The intersection of both sets.
    """
    intersection_set = cracking_set.intersection(rainbow_set)
    return intersection_set
