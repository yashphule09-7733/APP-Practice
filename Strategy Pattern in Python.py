from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using UPI")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")


# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


# Client
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)

cart = ShoppingCart(UPIPayment())
cart.checkout(250)

cart = ShoppingCart(PayPalPayment())
cart.checkout(500)