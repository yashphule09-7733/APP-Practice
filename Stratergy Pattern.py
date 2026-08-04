from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Concrete Strategy 2
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Concrete Strategy 3
class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


# Context
class ShoppingCart:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)


# Client Code
cart = ShoppingCart(CreditCardPayment())
cart.checkout(1500)

cart.set_payment_strategy(UPIPayment())
cart.checkout(800)

cart.set_payment_strategy(CashPayment())
cart.checkout(300)
