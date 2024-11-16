import unittest
from budget import Budget

class TestBudget(unittest.TestCase):
    def test_budget_creation(self):
        budget = Budget("Groceries", 500)
        self.assertEqual(budget.category, "Groceries")
        self.assertEqual(budget.limit, 500)

    def test_add_expense(self):
        budget = Budget("Groceries", 500)
        budget.add_expense(100)
        self.assertEqual(budget.spent, 100)
        budget.add_expense(450)
        self.assertEqual(budget.spent, 550)

if __name__ == "__main__":
    unittest.main()
