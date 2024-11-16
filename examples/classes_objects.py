"""  
Classes and Objects in Python
--------------------------------
Classes are blueprints for creating objects. Objects are instances of
class. 

Key Concepts:
- Defining a class using the `class` keyword.
- Create objects by instantiating a class.
"""

# Defining a class 
class Dog:
    """
    A simple class to represent a Dog
    """
    def __init__(self, name, breed):
        """
        constructor : Initializes the name and breed of the dog

        Args:
            name (_str_): name of the dog
            breed (_type_): breed of the dog
        """
        self.name = name
        self.breed = breed
    def bark(self):
        """
        Method : Print a message about the dog barks 
        """
        return f"{self.name} says woof!"

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog1.breed)  # Output: Golden Retriever
print(dog1.bark())  # Output: Buddy says woof!
print(dog2.name)  # Output: Max
print(dog2.breed)  # Output: Bulldog
print(dog2.bark())  # Output: Max says woof!
