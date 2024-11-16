"""
Expense Tracker using File Handling
-----------------------------------
This project demonstrates file handling by creating an expense tracker
to log and retrieve expenses.
"""

def log_expense(file_name, expense, amount):
    """
    Log an expense into the file.
    :param file_name: File to log the expense.
    :param expense: Description of the expense.
    :param amount: Amount spent.
    """
    with open(file_name, 'a') as file:
        file.write(f"{expense}: ${amount}\n")
        print(f"Logged expense: {expense} - ${amount}")

def view_expenses(file_name):
    """
    View all logged expenses.
    :param file_name: File containing the expense logs.
    """
    try:
        with open(file_name, 'r') as file:
            print(f"Expenses in {file_name}:\n{file.read()}")
    except FileNotFoundError:
        print(f"No expense log found. Start logging expenses!")

# Usage
file_name = "expenses.txt"
log_expense(file_name, "Coffee", 3.5)
log_expense(file_name, "Groceries", 45.0)
view_expenses(file_name)
