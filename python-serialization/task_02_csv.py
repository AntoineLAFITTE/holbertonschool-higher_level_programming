import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file by serializing its contents.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion is successful, False if an error occurs.
    """
    try:
        # Open the CSV file and read its content
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]  # Convert rows in list of dicts

        # Serialize the data and write it to a JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data from {csv_filename} has been converted to data.json.")
        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred during the conversion: {e}")
        return False
