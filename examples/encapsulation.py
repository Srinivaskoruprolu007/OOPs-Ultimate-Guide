"""
Encapsulation in Python
------------------------
Encapsulation is an OOP principle that restricts access to certain details of an object 
and allows access only through well-defined interfaces. It helps in keeping the internal 
state of an object safe from unauthorized access and modification.

Key Concepts:
- **Private attributes**: Variables that are meant to be accessed only within the class.
- **Public methods**: Functions that provide access to private attributes or methods.
- **Getter and Setter methods**: Special methods that allow controlled access to private attributes.

In Python, we can use a single underscore (_) for weak "protected" variables and 
a double underscore (__) for "private" variables that are less accessible outside the class.
"""

class BankAccount:
    """
    BankAccount class represents a bank account and encapsulates the balance of the account.
    The balance is a private attribute, and controlled access is provided through methods.
    """
    
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initializes the bank account with an account holder's name and an initial balance.
        
        Args:
            account_holder (str): Name of the account holder.
            initial_balance (float): Initial deposit for the account (default is 0.0).
        """
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance  # Private attribute (Encapsulated)

    def deposit(self, amount):
        """
        Deposits a certain amount to the account balance.
        
        Args:
            amount (float): The amount to be deposited.
            
        Returns:
            str: Message confirming the deposit.
        """
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. Current balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account balance.
        
        Args:
            amount (float): The amount to be withdrawn.
            
        Returns:
            str: Message confirming the withdrawal or an error message if insufficient funds.
        """
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid amount."

    def get_balance(self):
        """
        Returns the current balance of the account.
        
        Returns:
            float: The current balance.
        """
        return self.__balance

    def set_balance(self, amount):
        """
        Setter method for balance. Allows setting a new balance, but ensures the value is positive.
        
        Args:
            amount (float): The new balance to be set.
            
        Returns:
            str: Confirmation message or an error message if the amount is invalid.
        """
        if amount >= 0:
            self.__balance = amount
            return f"Balance updated. New balance: ${self.__balance}"
        else:
            return "Balance must be non-negative."

# Creating an object of BankAccount
account = BankAccount("John Doe", 1000)

# Depositing and withdrawing money
print(account.deposit(500))  # Depositing money
print(account.withdraw(200))  # Withdrawing money

# Trying to access private attribute (This will raise an error)
# print(account.__balance)  # Uncommenting this line will result in an AttributeError

# Using getter method to access balance
print(f"Current balance: ${account.get_balance()}")

# Using setter method to update balance
print(account.set_balance(1200))  # Setting new balance

