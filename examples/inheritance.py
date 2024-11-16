"""
Inheritance in Python
======================
Inheritance allows a class to inherit the attributes and methods of another class, promoting code reuse and creating a hierarchy of classes
Key Concepts:
- A subclass (child class) inherits from a superclass (parent class)
- A subclass can add its own attributes and methods or override methods from parent class
"""

# Parent Class
class Animal:
    def __init__(self, name, species):
        """
        Initialize an Animal object with name and species

        Args:
            name (str): name of the Animal
            species (str): species of the Animal
        """
        self.name = name
        self.species = species
    def speaks(self):
        raise NotImplementedError("Subclass must implement abstract method")

# child class (Subclass) inherits from a superclass (Animal class)
class Dog(Animal):
    def __init__(self, name, breed):
        """
        Initialize a Dog object with name and breed

        Args:
            name (str): name of the dog
            breed (str): breed of the dog
        """
    def speaks(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        """
        Initialize a Cat object with name and color

        Args:
            name (str): name of the cat
            color (str): color of the cat
        """
        super().__init__(name, species="Cat")
        self.color = color
    def speaks(self):
        return f"{self.name} says Meow!"

# Instantiate objects of Dog and Cat
my_dog = Dog("Fido", "Golden Retriever")
my_cat = Cat("Whiskers", "Black")

# Call thr speal method for each animal
print(my_dog.speaks())  # Output: Fido says Woof!
print(my_cat.speaks())  # Output: Whiskers says Meow!