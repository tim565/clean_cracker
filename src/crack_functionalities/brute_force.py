from hash_creator import hash_string
from itertools import product
from string import ascii_letters, digits


def brute_force(max_length, target_hash, include_digits=False, include_special_chars=False):
    """
        Attempts to brute-force a password by generating all possible combinations of characters up to a given length,
        and comparing their hash values to a target hash.

        Parameters:
        - max_length (int): The maximum length of the password to be brute-forced.
        - target_hash (str): The hash value of the password that needs to be found.
        - include_digits (bool, optional): If set to True, digits (0-9) are included in the character set.
          Default is False.
        - include_special_chars (bool, optional): If set to True, special characters ('?!#') are included in the
          character set. Default is False.

        Returns:
        - (bool, str): A tuple where the first element is a boolean indicating whether the brute force was successful,
          and the second element is the discovered password if successful, or an empty string otherwise.
    """

    # Define the character set
    charset = ascii_letters
    if include_digits==True:
        charset += digits
    if include_special_chars==True:
        charset += '?!#'

    # Iterate over all possible lengths
    for length in range(1, max_length + 1):
        # Generate all possible combinations of the current length
        for combination in product(charset, repeat=length):
            combination_string = ''.join(combination)
            combination_hash = hash_string(combination_string, hash_algorithm='sha256')

            if combination_hash == target_hash:
                return True, combination_string

    return False, ''



if __name__ == "__main__":
    # Example usage

    pw_max_length = 4
    pw_target_hash = hash_string('moin', 'sha256')
    print('The hash value of the password that needs to be found is: ', pw_target_hash)
    print()
    success, password = brute_force(pw_max_length , pw_target_hash, include_digits=False, include_special_chars=False)

    if success:
        print('The underlying password for the given hash is: ', password)
    else:
        print('Brute forcing the password for the given hash was not successful. Try to inclde more characters, ' +
              'a bigger lenght or a different hashing method.')
