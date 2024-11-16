"""
User class for managing users and permissions.
"""
class User:
    def __init__(self, username, role="normal"):
        self.username = username
        self.role = role  # admin or normal

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"
