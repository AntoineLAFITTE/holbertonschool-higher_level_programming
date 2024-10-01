import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and saves it to a file.

    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the file where the XML will be saved.
    """
    # Create the root element
    root = ET.Element('data')

    # Iterate through the dictionary and add child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert values to string for XML storage

    # Write the XML tree to a file
    tree = ET.ElementTree(root)
    tree.write(filename)
    print(f"Dictionary serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to be deserialized.

    Returns:
        dict: A dictionary with the deserialized XML data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary
        deserialized_data = {child.tag: child.text for child in root}

        return deserialized_data

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

    except ET.ParseError:
        print(f"Error: Failed to parse the XML file {filename}.")
        return None
