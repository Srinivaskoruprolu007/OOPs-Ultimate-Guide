"""
Abstraction in Python
----------------------
Abstraction is the process of hiding the internal details and showing only the necessary functionality to the user.
In Python, abstraction is achieved through abstract classes and methods using the `abc` module.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract base class for vehicles. This class defines the structure for all derived vehicle classes.
    """

    @abstractmethod
    def start_engine(self):
        """
        Abstract method to start the engine of the vehicle.
        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def stop_engine(self):
        """
        Abstract method to stop the engine of the vehicle.
        Must be implemented by all subclasses.
        """
        pass

class Car(Vehicle):
    """
    A concrete class that represents a Car. Inherits from the abstract Vehicle class.
    """
    def start_engine(self):
        """
        Implementation of the abstract method to start the car engine.
        """
        print("Car engine started.")

    def stop_engine(self):
        """
        Implementation of the abstract method to stop the car engine.
        """
        print("Car engine stopped.")

class Motorcycle(Vehicle):
    """
    A concrete class that represents a Motorcycle. Inherits from the abstract Vehicle class.
    """
    def start_engine(self):
        """
        Implementation of the abstract method to start the motorcycle engine.
        """
        print("Motorcycle engine started.")

    def stop_engine(self):
        """
        Implementation of the abstract method to stop the motorcycle engine.
        """
        print("Motorcycle engine stopped.")

# Creating objects of concrete classes
car = Car()
motorcycle = Motorcycle()

# Using the methods
car.start_engine()
car.stop_engine()

motorcycle.start_engine()
motorcycle.stop_engine()
