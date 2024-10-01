import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to be serialized and saved.
        filename (str): The name of the JSON file where the data will be saved

    If the file already exists, it will be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data has been serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        dict: A dictionary containing the deserialized data from the JSON file
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
