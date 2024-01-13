import unittest
from ...src.crack_functionalities.hash_creator import hash_values


class TestHashValuesFunction(unittest.TestCase):

    def test_sha256_hashing(self):
        input_values = ['password1', 'secret123', 'example456']
        hashed_values = hash_values(input_values, hash_algorithm='sha256')

        expected_hashes = [
            'e38ad214943daad1d64c102faec29de4afe9da3d3d605ccd849c4395',
            'e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4a50aae654c2e850',
            'f1be93bea4ccef4cfb2442f4e18d466b7b8a502450b25c6eb2e49ea2'
        ]

        self.assertEqual(hashed_values, expected_hashes)

    def test_md5_hashing(self):
        input_values = ['password1', 'secret123', 'example456']
        hashed_values = hash_values(input_values, hash_algorithm='md5')

        expected_hashes = [
            '5f4dcc3b5aa765d61d8327deb882cf99',
            '641d2aed121f1d1505541ca97e91a244',
            '1a79a4d60de6718e8e5b326e338ae533'
        ]

        self.assertEqual(hashed_values, expected_hashes)


if __name__ == '__main__':
    unittest.main()
