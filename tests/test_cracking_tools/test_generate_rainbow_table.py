import unittest
import os
from src.cracking_tools.generate_rainbow_table import list_to_list_of_dicts, get_cleartext_password_list,\
    generate_table_with_hashes, generate_rainbow_table


class TestHashFunctions(unittest.TestCase):

    def test_list_to_list_of_dicts(self):
        """
        Ensures two-dimensional lists are correctly converted to a list of dictionaries.
        """
        two_dimensional_list = [["Alice", "Bob"], [25, 30]]
        keys = ["name", "age"]
        expected_output = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
        self.assertEqual(list_to_list_of_dicts(two_dimensional_list, keys), expected_output)

    def test_get_cleartext_password_list(self):
        """
        Verifies extraction of cleartext passwords from a CSV file.
        """
        test_file_path = '../resources/input/raw_passwords.csv'
        expected_output = ["password_1", "password_2", "password_3"]
        self.assertEqual(get_cleartext_password_list(test_file_path), expected_output)

    def test_generate_table_with_hashes(self):
        """
        Checks if a table of hashed passwords is generated correctly.
        """
        cleartext_password_list = ["pass1", "pass2"]
        user_given_hash_algorithms_list = ["md5", "sha256"]
        result = generate_table_with_hashes(cleartext_password_list, user_given_hash_algorithms_list)
        self.assertEqual(len(result), 2)
        self.assertTrue("md5" in result[0] and "sha256" in result[0])

    def test_generate_rainbow_table(self):
        """
        Tests the generation of a rainbow table and its output to a file.
        """
        password_list_file_path = '../resources/input/raw_passwords.csv'
        generate_rainbow_table(password_list_file_path, testing=True)
        expected_output_file = "../resources/expected_output/generated_rainbow_table.csv"
        self.assertTrue(os.path.exists(expected_output_file))
        # Cleanup (optional)
        os.remove(expected_output_file)


if __name__ == '__main__':
    unittest.main()