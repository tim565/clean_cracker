import unittest
import hashlib
from src.utility_functions.helper_functions import get_hash_type, get_hash_types_from_set, process_user_input


class TestHelperFunctions(unittest.TestCase):

    def test_md5(self):
        """
        Test case for checking if the get_hash_type function correctly identifies an MD5 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.md5(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "md5")

    def test_sha1(self):
        """
        Test case for checking if the get_hash_type function correctly identifies a SHA-1 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.sha1(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "sha1")

    def test_sha224(self):
        """
        Test case for checking if the get_hash_type function correctly identifies a SHA-224 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.sha224(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "sha224")

    def test_sha256(self):
        """
        Test case for checking if the get_hash_type function correctly identifies a SHA-256 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.sha256(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "sha256")

    def test_sha384(self):
        """
        Test case for checking if the get_hash_type function correctly identifies a SHA-384 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.sha384(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "sha384")

    def test_sha512(self):
        """
        Test case for checking if the get_hash_type function correctly identifies a SHA-512 hash.
        """
        input_string = "password"
        hash_to_test = hashlib.sha512(input_string.encode()).hexdigest()
        self.assertEqual(get_hash_type(hash_to_test), "sha512")

    def test_unknown_hash_type(self):
        """
        Test case for checking if the get_hash_type function correctly identifies an unknown hash type.
        """
        hash_to_test = "not_a_hash"  # Arbitrary hash with length not in the dictionary
        self.assertEqual(get_hash_type(hash_to_test), "Unknown Hash Type")

    def test_get_hash_types_from_set(self):
        """
        Ensures correct identification of hash types from a set of hash strings.
        """
        hash_set = {"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # sha256 hash of "password"
                    "5f4dcc3b5aa765d61d8327deb882cf99"}  # md5 hash of "password"
        expected_types = ['sha256', 'md5']

        result = get_hash_types_from_set(hash_set)
        self.assertListEqual(result, expected_types)

    def test_process_user_input(self):
        """
        Verifies the standardization of various hash algorithm name formats.
        """
        inputs_and_expected = {
            "Sha-256": "sha256",
            "SHA-256": "sha256",
            "sha 256": "sha256",
            "sha256": "sha256"
        }

        for input_str, expected in inputs_and_expected.items():
            self.assertEqual(process_user_input(input_str), expected)


if __name__ == "__main__":
    unittest.main()
