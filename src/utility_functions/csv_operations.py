import os
import re
import csv


def write_dicts_to_csv(data_list, csv_path):
    """
    Writes a list of dictionaries to a CSV file.

    Parameters:
    - data_list (list of dict): The list of dictionaries to be written to the CSV file.
    - csv_path (str): The path to the CSV file.
    """
    try:
        # Add counter to outpt file name
        csv_path = get_output_file_name(csv_path)
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data_list[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the data
            for row_dict in data_list:
                writer.writerow(row_dict)

        print(f"CSV file '{csv_path}' has been successfully created.")
    except Exception as e:
        print(f'An error occurred while writing to the CSV file: {e}')


def get_output_file_name(file_path):
    # If the file does not exist, return the original file path
    if not os.path.exists(file_path):
        return file_path

    directory, file_name = os.path.split(file_path)
    file_base, file_extension = os.path.splitext(file_name)

    # Regular expression to identify and separate the counter at the end of the file name
    # It looks for an underscore followed by digits at the end of the file name
    match = re.search(r'(.*?)_(\d+)$', file_base)

    if match:
        base_name, number = match.groups()
    else:
        base_name = file_base
        number = 0

    counter = int(number)
    new_file_path = file_path

    # Iterate to find the highest existing counter
    while os.path.exists(new_file_path):
        counter += 1
        new_file_name = f'{base_name}_{counter}{file_extension}'
        new_file_path = os.path.join(directory, new_file_name)

    return new_file_path


def read_csv_create_list(csv_path, column_name):
    """
       Reads a CSV file and extracts values from a specified column into a list.

       Parameters:
       - csv_path (str): The path to the CSV file.
       - column_name (str): The name of the column from which values will be extracted.

       Returns:
       - list or None: A list containing values from the specified column, or None if an error occurs.

       The function reads the contents of the CSV file located at `csv_path` and extracts values
       from the column with the name `column_name`. The extracted values are stored in a list, which
       is then returned.
       """
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Check if the column_name is in the header
        assert column_name in reader.fieldnames, f"Error: Column '{column_name}' not found in the CSV file."

        values_list = []
        # Iterate through rows and append the column values to the list
        for row in reader:
            values_list.append(row[column_name])

    return values_list


def read_csv_create_dictionary_list(csv_path):
    """
    Reads a CSV file, removes the Byte Order Mark (BOM) caused by some encodings,
    and processes the content into a list of dictionaries.

    Parameters:
    - csv_path (str): The path to the CSV file.

    Returns:
    - list: A list of dictionaries, where each dictionary represents a row in the CSV file.
      The keys are column names, and the values are corresponding data in each row.
    """
    # Read CSV file and manually remove BOM caused by some encodings
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        content = csvfile.read()
        if content.startswith('\ufeff'):
            content = content[1:]

    # Process the content into a list of dictionaries
    csv_reader = csv.DictReader(content.splitlines())

    # Convert the reader object to a list of dictionaries and return it
    data_list = list(csv_reader)
    return data_list


def extract_column_of_former_csv_to_set(list_of_dictionaries, column_name):
    """
    Extract a specific column from a list of dictionaries and convert it to a set.

    Parameters:
    - list_of_dictionaries: List of dictionaries representing the CSV data.
    - column_name: Name of the column to extract.

    Returns:
    - A set containing the values of the specified column.
    """
    assert any(column_name in row for row in list_of_dictionaries), \
        f"Column '{column_name}' not found in any dictionary."
    column_set = set()

    # Iterates through the dictionary and collects all values of the specified column
    for row in list_of_dictionaries:
        if column_name in row:
            column_set.add(row[column_name])
    return column_set
