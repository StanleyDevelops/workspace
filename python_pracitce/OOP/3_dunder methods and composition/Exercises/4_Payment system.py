# Real world use of Abstract classes
# polymorphism + abstract classes together

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process(self):     # every payment type MUST implement this
        pass

    @abstractmethod
    def validate(self):    # every payment type MUST implement this
        pass

    def receipt(self):     # shared method, no override needed
        print(f"Payment of ₹{self.amount} processed.")

class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process(self):
        print(f"Processing ₹{self.amount} via UPI: {self.upi_id}")

    def validate(self):
        return "@" in self.upi_id

class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        print(f"Processing ₹{self.amount} via Credit Card: **** **** **** {self.card_number[-4:]}")

    def validate(self):
        return len(self.card_number) == 16

class NetBanking(Payment):
    def __init__(self, amount, account_number):
        super().__init__(amount)
        self.account_number = account_number

    def process(self):
        print(f"Processing ₹{self.amount} via NetBanking: *** *** ***{self.account_number[-2:]}")

    def validate(self):
        return len(self.account_number) == 11


# Testing objects

payments = [UPI(500, "stanley@upi"),
            CreditCard(1000, "1234567890123456"),
            NetBanking(15000, "12345678123")]

for payment in payments:
    if payment.validate():
        payment.process()
        payment.receipt()
    else:
        print("Invalid payment details!")
