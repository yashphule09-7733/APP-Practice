class Payment:
    def pay(self, payment_type, amount):
        if payment_type == "CreditCard":
            print(f"Paid ₹{amount} using Credit Card")
        elif payment_type == "UPI":
            print(f"Paid ₹{amount} using UPI")
        else:
            print("Invalid Payment Method")


payment = Payment()
payment.pay("CreditCard", 1000)
payment.pay("UPI", 500)
