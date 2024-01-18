import unittest
from src.cracking_tools.hash_creator import hash_list


class TestHashCreatorFunction(unittest.TestCase):

    def test_sha256_hashing(self):
        """
        Test the hash_values function with SHA256 algorithm.

        This test case verifies that the hash_values function correctly hashes the input values using the SHA256 algorithm.
        It compares the hashed values returned by the function with the expected hashes and asserts that they are equal.
        """
        input_values = ['password1', 'secret123', 'example456']
        hashed_values = hash_list(input_values, hash_algorithm='sha256')

        expected_hashes = [
            'e38ad214943daad1d64c102faec29de4afe9da3d3d605ccd849c4395',
            'e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4a50aae654c2e850',
            'f1be93bea4ccef4cfb2442f4e18d466b7b8a502450b25c6eb2e49ea2'
        ]

        self.assertEqual(hashed_values, expected_hashes)

    def test_md5_hashing(self):
        
        """
        Test the hash_values function with MD5 algorithm.

        This test case verifies that the hash_values function correctly hashes the input values using the MD5 algorithm.
        It compares the hashed values returned by the function with the expected hashes and asserts that they are equal.
        """
        
        input_values = ['password1', 'secret123', 'example456']
        hashed_values = hash_list(input_values, hash_algorithm='md5')

        expected_hashes = [
            '5f4dcc3b5aa765d61d8327deb882cf99',
            '641d2aed121f1d1505541ca97e91a244',
            '1a79a4d60de6718e8e5b326e338ae533'
        ]

        self.assertEqual(hashed_values, expected_hashes)


if __name__ == '__main__':
    unittest.main()
