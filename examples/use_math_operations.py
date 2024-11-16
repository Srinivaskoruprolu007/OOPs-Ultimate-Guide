"""
use_math_operations.py

This script demonstrates the usage of the custom module `math_operations`.
It performs basic mathematical operations like addition, subtraction, multiplication, and division.
"""

# Importing the custom module
from math_operations import add, subtract, multiply, divide

def main():
    """
    Main function to demonstrate the custom math_operations module.
    """
    # Input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform operations
    print(f"\nAddition of {num1} and {num2}: {add(num1, num2)}")
    print(f"Subtraction of {num1} from {num2}: {subtract(num1, num2)}")
    print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
    
    try:
        print(f"Division of {num1} by {num2}: {divide(num1, num2)}")
    except ValueError as e:
        print(f"Error during division: {e}")

if __name__ == "__main__":
    main()
