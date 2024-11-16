"""
Shape Drawing System using Polymorphism
--------------------------------------
In this project, we use polymorphism to draw different shapes. Each shape (Circle, Square, Triangle) 
implements the `draw()` method, demonstrating polymorphism in action.
"""

import math

# Base class Shape
class Shape:
    """
    Base class for all shapes. Provides a basic draw method.
    """
    def draw(self):
        """
        Draw the shape. This method should be overridden by child classes.

        Raises:
            NotImplementedError: Not implemented
        """
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass Circle
class Circle(Shape):
    """
    Circle shape. Implements the draw method.
    Args:
        Shape (shape): Shape is a class (base class)
    """
    def __init__(self, radius):
        """
        initialize the shape(circle) with radius 
        Args:
            radius (float): radius of the class
        """
        self.radius = radius

    def draw(self):
        """
        Draw the circle using the radius.
        """
        print(f"Drawing a circle with radius {self.radius}.")

# Subclass Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def draw(self):
        print(f"Drawing a square with side length {self.side_length}.")

# Subclass Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        print(f"Drawing a triangle with base {self.base} and height {self.height}.")

# List of shapes
shapes = [
    Circle(5),
    Square(4),
    Triangle(3, 4)
]

# Drawing all shapes using polymorphism
for shape in shapes:
    shape.draw()  # This calls the appropriate draw() method for each shape
