import json

def save_data(data, filename="data.json"):
    """
    Save data (transactions, budgets) to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data(filename="data.json"):
    """
    Load data (transactions, budgets) from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
