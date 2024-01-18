import unittest
from src.cracking_tools.brute_force import brute_force
from src.cracking_tools.hash_creator import hash_string


class TestBruteForce(unittest.TestCase):

    def test_brute_force_success(self):
        """
        Test case where the brute force should succeed.
        """
        # Given
        password = 'abc'
        hash_of_password = hash_string(password, 'sha256')  # Assuming hash_string function is accessible
        max_length = 3

        # When
        success, found_password = brute_force(max_length, hash_of_password, include_digits=False,
                                              include_special_chars=False)

        # Then
        self.assertTrue(success)
        self.assertEqual(found_password, password)

    def test_brute_force_success_with_special_chars_and_digits(self):
        """
        Test case where the brute force should succeed with special characters and digits included.
        """
        # Given
        password = 'a1!b'
        hash_of_password = hash_string(password, 'sha256')  # Replace with the correct hashing function call
        max_length = 4

        # When
        success, found_password = brute_force(max_length, hash_of_password, include_digits=True,
                                              include_special_chars=True)

        # Then
        self.assertTrue(success)
        self.assertEqual(found_password, password)

    def test_brute_force_failure(self):
        """
        Test case where the brute force should fail due to insufficient max_length.
        """
        # Given
        password = 'abcd'
        hash_of_password = hash_string(password, 'sha256')
        max_length = 3  # Deliberately set to less than the length of the password

        # When
        success, found_password = brute_force(max_length, hash_of_password, include_digits=False,
                                              include_special_chars=False)

        # Then
        self.assertFalse(success)
        self.assertEqual(found_password, '')


if __name__ == '__main__':
    unittest.main()