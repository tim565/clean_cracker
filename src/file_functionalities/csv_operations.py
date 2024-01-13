import csv


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
    with open(csv_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if content.startswith('\ufeff'):
            content = content[1:]

    # Process the content into a list of dictionaries
    csv_reader = csv.DictReader(content.splitlines())

    # Convert the reader object to a list of dictionaries and return it
    data_list = list(csv_reader)
    return data_list


def extract_column_to_set(list_of_dictionaries, column_name):
    """
    Extract a specific column from a list of dictionaries and convert it to a set.

    Parameters:
    - list_of_dictionaries: List of dictionaries representing the CSV data.
    - column_name: Name of the column to extract.

    Returns:
    - A set containing the values of the specified column.
    """
    column_set = set()

    # Iterates through the dictionary and collects all values of the specified column
    for row in list_of_dictionaries:
        if column_name in row:
            column_set.add(row[column_name])
    return column_set
