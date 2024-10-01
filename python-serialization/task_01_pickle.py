import pickle


class CustomObject:
    """
    A custom class representing an object with the following attributes:

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.

    Methods:
        display(): Prints the attributes of the object.
        serialize(filename): Serializes the object and saves it
        to the provided filename.
        deserialize(cls, filename): Deserializes and loads an object
        from the provided filename.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of CustomObject and saves it to a file.

        Args:
            filename (str): The name of the file where the object will
            be serialized and saved.

        If the file already exists, it will be replaced.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object has been serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"An error occurred during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes and loads an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file from which
            to deserialize the object.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"An error occurred during deserialization: {e}")
            return None
