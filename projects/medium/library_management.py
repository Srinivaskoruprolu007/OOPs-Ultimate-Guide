"""
Library Management System using Inheritance
-------------------------------------------
This project demonstrates the use of inheritance to manage roles in a library system.
"""

class Person:
    """
    Base class representing a person in the library.
    """
    def __init__(self, name):
        self.name = name

class Admin(Person):
    """
    Admin role, inherits from Person.
    """
    def __init__(self, name):
        super().__init__(name)
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.
        """
        self.books.append(book)
        print(f"Admin {self.name} added the book: {book}")

class Member(Person):
    """
    Member role, inherits from Person.
    """
    def borrow_book(self, book, admin):
        """
        Borrows a book from the library if available.
        """
        if book in admin.books:
            admin.books.remove(book)
            print(f"Member {self.name} borrowed the book: {book}")
        else:
            print(f"Sorry, {self.name}, the book '{book}' is not available.")

# Simulating the library system
admin = Admin("Alice")
member = Member("Bob")

# Admin adds books
admin.add_book("Python Programming")
admin.add_book("Data Science Handbook")

# Member borrows books
member.borrow_book("Python Programming", admin)
member.borrow_book("Machine Learning Basics", admin)
