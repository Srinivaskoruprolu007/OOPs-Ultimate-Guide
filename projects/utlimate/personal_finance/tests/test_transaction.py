import unittest
from transaction import Transaction
from category import Category

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        category = Category("Groceries")
        transaction = Transaction(100, category, "expense", "Buying food")
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.transaction_type, "expense")
        self.assertEqual(transaction.description, "Buying food")

    def test_category_total(self):
        category = Category("Groceries")
        category.add_transaction(Transaction(100, category, "expense"))
        category.add_transaction(Transaction(50, category, "expense"))
        self.assertEqual(category.total(), 150)

if __name__ == "__main__":
    unittest.main()
