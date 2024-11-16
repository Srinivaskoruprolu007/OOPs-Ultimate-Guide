"""
Employee Management System using Encapsulation
---------------------------------------------
In this project, we use encapsulation to manage employee details, such as their name, 
position, and salary, within the Employee class. Only authorized methods can modify the 
employee data.
"""

class Employee:
    """
    Employee class encapsulates employee details and provides methods to access and update the data.
    """

    def __init__(self, name, position, salary):
        """
        Initializes the employee with their name, position, and salary.
        
        Args:
            name (str): Employee's name.
            position (str): Employee's position or job title.
            salary (float): Employee's salary.
        """
        self.__name = name  # Private attribute
        self.__position = position  # Private attribute
        self.__salary = salary  # Private attribute

    def get_employee_details(self):
        """
        Returns a dictionary with the employee's details.
        
        Returns:
            dict: A dictionary containing the employee's name, position, and salary.
        """
        return {
            "Name": self.__name,
            "Position": self.__position,
            "Salary": self.__salary
        }

    def update_position(self, new_position):
        """
        Updates the employee's position.
        
        Args:
            new_position (str): The new position to assign to the employee.
            
        Returns:
            str: Confirmation message.
        """
        self.__position = new_position
        return f"Position updated to: {self.__position}"

    def update_salary(self, new_salary):
        """
        Updates the employee's salary if the new salary is greater than the current salary.
        
        Args:
            new_salary (float): The new salary to assign to the employee.
            
        Returns:
            str: Confirmation message or error message.
        """
        if new_salary > self.__salary:
            self.__salary = new_salary
            return f"Salary updated to: ${self.__salary}"
        else:
            return "New salary must be higher than the current salary."

# Create Employee instance
employee = Employee("Jane Doe", "Software Engineer", 70000)

# Get employee details
print(employee.get_employee_details())

# Update position
print(employee.update_position("Senior Software Engineer"))

# Update salary
print(employee.update_salary(75000))
