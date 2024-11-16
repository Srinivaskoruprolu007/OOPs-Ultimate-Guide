from transaction import Transaction
from category import Category
from budget import Budget
from user import User
from utils.file_handler import save_data, load_data

def main():
    user = User("john_doe", "normal")
    groceries = Category("Groceries")
    budget = Budget("Groceries", 500)

    # Create some transactions
    groceries.add_transaction(Transaction(100, groceries, "expense", "Groceries shopping"))
    groceries.add_transaction(Transaction(200, groceries, "expense", "More shopping"))

    # Track spending against budget
    budget.add_expense(groceries.total())

    # Save data
    data = {"transactions": [str(t) for t in groceries.transactions], "budget": str(budget)}
    save_data(data)

    # Load data
    loaded_data = load_data()
    print("Loaded Data:", loaded_data)

if __name__ == "__main__":
    main()
