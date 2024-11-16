"""
Employee Hierarchy System
==========================
An example of a how inheritance can be used to manage employees with different roles.
"""

# Parent Class 
class Employee:
    def __init__(self, name, employee_id):
        """
        Initialize an Employee object.

        Args:
            name (str): name of the employee
            employee_id (int): employee id of the employee
        """
        self.name = name
        self.employee_id = employee_id
    def details(self):
        """
        Return a string containing the employee's details.
        """
        return f"Name: {self.name}, Employee ID: {self.employee_id}"

# Child Class 1 : Manager
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        """
        Initialize an Manager object.
        Args:
            name (str): name of the Manager
            employee_id (int): employee id of the Manager
            department (_type_): department of the manager
        """
        super().__init__(name, employee_id)
        self.department = department
    
    def details(self):
        """
        Return a string containing the manager's details.
        """
        return f"{super().details()}, Department: {self.department}"
    
# Child Class 2: Developer
class Developer(Employee):
    def __init__(self, name, employee_id, programming_languages):
        """
        Initialize a Developer object
        Args:
            name (str): name of the Developer
            employee_id (int): employee_id of the Developer
            programming_languages (str): programming language used by developer
        """
        super().__init__(name, employee_id)
        self.programming_languages = programming_languages
    def details(self):
        """
        Return a string containing the details of the Developer
        Returns:
            str: String representation of developer
        """
        return super().details()+ f", Programming Languages: {self.programming_languages}"
    
# create instances of Developer and Manager
dev1 = Developer("John Doe", 123, "Python, Java, C++")
dev2 = Developer("Jane Doe", 456, "JavaScript, Ruby, Swift")
manager1 = Manager("Alice Smith", 789, "HR")
print(dev1.details())
print(dev2.details())
print(manager1.details())
