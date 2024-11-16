""" 
Personal Expense Tracker 
=======================
A simple project to demonstrate classes and objects.
Track expenses and categorizes them.
"""
class Expense:
    """ 
    Represents an individual expense
    """
    def __init__(self,amount, category, description=""):
        """
        Initializes an Expense object.
        Args:
            amount (float): amount had spent
            category (str): category of the expense
            description (str, optional): additional comments to the expense. Defaults to "".
        """
        self.amount = amount
        self.category = category
        self.description = description
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Expense object.

        Returns:
            str: string representation of the Expense object
        """
        return f"Expense: {self.category}, Amount: {self.amount}, Description: {self.description}"
    


class ExpenseTracker:
    """
    Tracks and manages multiple Expenses
    """
    def __init__(self):
        """
        Initializes an ExpenseTracker object.
        """
        self.expenses = []
    def add_expenses(self, expense):
        """
        Adds and expense to the tracker

        Args:
            expense (Expense): Expense type (user defined class)
        """
        self.expenses.append(expense)
        
    def view_expenses(self):
        """
        Display all expenses
        """
        if not self.expenses:
            print("No expenses to display")
        for expense in self.expenses:
            print(expense)
        
    def total_by_category(self, category):
        """
        Calculate the total amount spent in a specific category

        Args:
            category (str): Category of the expenses
        """
        return sum(exp.amount for exp in self.expenses if exp.category == category)
    
# Main program
if __name__ == '__main__':
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu...")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Category")
        print("4. Exit")
        
        choice = input("Choose an options")
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., food, travel): ")
            description = input("Enter description (optional): ")
            tracker.add_expenses(Expense(amount, category, description))
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter category: ")
            print(f"Total for {category}: {tracker.total_by_category(category)}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose valid option.")
        