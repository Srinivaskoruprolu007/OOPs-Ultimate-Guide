"""
Polymorphism in Python
-----------------------
Polymorphism allows us to use a common interface for different types of objects. 
It enables us to call methods of different classes using the same method name, 
even if those methods have different implementations in each class.

Key Concepts:
- **Method Overloading**: Multiple methods with the same name but different parameters (Python doesn't support traditional method overloading, but we can use default arguments).
- **Method Overriding**: Subclasses provide their own implementation of methods defined in the parent class.
"""

class Animal:
    def sound(self):
        """
            give a string representation of sound by animal
        Returns:
            str : string representation of sound
        """
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        """
            return a string representation of dog sound
        Returns:
            str: string representation of dog sound
        """
        return "Woof!"

class Cat(Animal):
    def sound(self):
        """
            return a string representation of a cat
        Returns:
            str : string representation of cat' sound
        """
        return "Meow!"

class Cow(Animal):
    def sound(self):
        """
            returns a string representation of cow sound
        Returns:
            str : string representation of cow's sound
        """
        return "Moo!"

def make_sound(animal: Animal):
    """
    This function accepts any object that is an instance of the Animal class or its subclasses,
    and calls the `sound()` method on it. This demonstrates polymorphism.
    """
    print(animal.sound())

# Instantiate objects of Dog, Cat, and Cow
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism to call the same method for different types of animals
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
make_sound(cow)  # Output: Moo!
