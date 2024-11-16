"""
Budget class for setting and tracking budgets for categories.
"""
class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print(f"Warning: You have exceeded the budget for {self.category}")

    def __str__(self):
        return f"Budget for {self.category}: {self.spent}/{self.limit}"
