"""
Category class for organizing transactions.
"""
from projects.utlimate.personal_finance.transaction import Transaction


class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
        else:
            raise ValueError("Must add a Transaction instance")

    def total(self):
        return sum(t.amount for t in self.transactions)

    def __str__(self):
        return f"Category: {self.name} | Total: {self.total()}"
