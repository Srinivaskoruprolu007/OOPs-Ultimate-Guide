"""
Transaction class for storing transaction data (income/expense)
"""
from datetime import datetime

class Transaction:
    def __init__(self, amount, category, transaction_type, description=""):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type  # 'income' or 'expense'
        self.description = description
        self.date = datetime.now()

    def __str__(self):
        return f"{self.date} - {self.transaction_type.capitalize()} - {self.category}: {self.amount} ({self.description})"
