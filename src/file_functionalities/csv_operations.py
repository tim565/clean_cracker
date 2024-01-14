import csv


def write_dicts_to_csv(data_list, csv_path):
    """
    Writes a list of dictionaries to a CSV file.

    Parameters:
    - data_list (list of dict): The list of dictionaries to be written to the CSV file.
    - csv_path (str): The path to the CSV file.
    """
    try:
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
        print(f"An error occurred while writing to the CSV file: {e}")


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
        if column_name not in reader.fieldnames:
            print(f"Error: Column '{column_name}' not found in the CSV file.")
            return None

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
