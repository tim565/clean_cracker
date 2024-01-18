import unittest
import os
from src.utility_functions.csv_operations import write_dicts_to_csv, get_output_file_name, read_csv_create_list,\
    read_csv_create_dictionary_list, extract_column_of_former_csv_to_set


class TestCSVFunctions(unittest.TestCase):

    def test_write_dicts_to_csv(self):
        """
        Tests writing a list of dictionaries to a CSV file.
        """
        test_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        test_csv_path = 'test_output.csv'
        write_dicts_to_csv(test_data, test_csv_path)
        self.assertTrue(os.path.exists(test_csv_path))
        # Cleanup
        os.remove(test_csv_path)

    def test_get_output_file_name(self):
        """
        Validates file naming for non-existent paths to avoid overwriting.
        """
        test_file_path = 'test_file.csv'
        output_file_path = get_output_file_name(test_file_path)
        # Assuming test_file.csv does not exist
        self.assertEqual(output_file_path, test_file_path)

    def test_read_csv_create_list(self):
        """
        Checks extraction of column values into a list from a CSV file.
        """
        test_csv_path = '../resources/input/raw_passwords_2.csv'
        test_column_name = 'Name'
        expected_output = ['Der Boss', 'Lämchen', 'Schmitz']
        self.assertEqual(read_csv_create_list(test_csv_path, test_column_name), expected_output)

    def test_read_csv_create_dictionary_list(self):
        """
        Ensures correct conversion of a CSV file into a list of dictionaries.
        """
        test_csv_path = '../resources/input/hacked_database_table.csv'
        expected_output = [{'name': 'Alice', 'age': '30', 'password': '73'},
                           {'name': 'Bob', 'age': '25', 'password': '7373'}]
        self.assertEqual(read_csv_create_dictionary_list(test_csv_path), expected_output)

    def test_extract_column_of_former_csv_to_set(self):
        """
        Tests extracting values of a specific column from a list of dictionaries into a set.
        """
        test_list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        test_column_name = 'name'
        expected_output = {'Alice', 'Bob'}
        self.assertEqual(extract_column_of_former_csv_to_set(test_list_of_dicts, test_column_name), expected_output)


if __name__ == '__main__':
    unittest.main()