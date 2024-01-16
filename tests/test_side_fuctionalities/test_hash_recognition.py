import unittest



class TestGetHashType(unittest.TestCase):
    """
    A test case class for testing the get_hash_type function.
    """

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


if __name__ == "__main__":
    unittest.main()
