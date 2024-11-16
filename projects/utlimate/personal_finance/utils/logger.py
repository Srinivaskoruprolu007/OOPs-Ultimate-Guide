from functools import wraps
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

def log_transaction(func):
    """
    Decorator to log every transaction (income/expense).
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Transaction made: {args[0]} - {args[1]}")
        return result
    return wrapper
