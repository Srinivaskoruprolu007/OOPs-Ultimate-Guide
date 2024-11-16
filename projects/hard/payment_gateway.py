"""
Payment Gateway System using Abstraction
----------------------------------------
This project simulates a payment gateway system where different payment methods 
inherit from an abstract Payment class and implement their payment processing logic.
"""

from abc import ABC, abstractmethod

class Payment(ABC):
    """
    Abstract class that defines the structure for all payment methods.
    """
    @abstractmethod
    def process_payment(self, amount):
        """
        Abstract method to process a payment of a given amount.
        """
        pass

class CreditCardPayment(Payment):
    """
    A concrete class that implements payment processing via credit card.
    """
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}.")

class PayPalPayment(Payment):
    """
    A concrete class that implements payment processing via PayPal.
    """
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}.")

class BankTransferPayment(Payment):
    """
    A concrete class that implements payment processing via bank transfer.
    """
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}.")

# Simulating payments
payment_methods = [
    CreditCardPayment(),
    PayPalPayment(),
    BankTransferPayment()
]

for method in payment_methods:
    method.process_payment(100)  # Process $100 payment using each method
