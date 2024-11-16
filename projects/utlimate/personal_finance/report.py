"""
Functions to generate various reports based on transactions.
"""
def generate_monthly_report(transactions):
    """
    Generates a monthly report of income and expenses.
    :param transactions: List of transactions
    """
    income = sum(t.amount for t in transactions if t.transaction_type == "income")
    expense = sum(t.amount for t in transactions if t.transaction_type == "expense")
    return f"Monthly Report: Income: {income}, Expense: {expense}, Net Balance: {income - expense}"
