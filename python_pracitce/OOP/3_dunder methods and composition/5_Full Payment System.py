# Full Payment system

from abc import ABC, abstractmethod
class Payment(ABC):

    def __init__(self, amount, status = "pending"):
        self.amount = amount
        self.status = status

    def __str__(self):
        return f"Current amount: {self.amount} || Status: {self.status}"
    
    @abstractmethod           # Every child must implement
    def process(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def receipt(self):        # may or may not be overriden by child 
        print(f"Payment of amount ₹{self.amount} processed.")

class UPI(Payment):

   # extra attribute = upi_id
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    # define process for UPI and set status to completed
    def process(self):
        print(f"Processing ₹{self.amount} via UPI...")
        self.status = "completed"

    def validate(self):
        return "@" in self.upi_id

class CreditCard(Payment):

    # extra attribute = card_number
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        print(f"Processing amount ₹{self.amount} via CreditCard: **** **** **** {self.card_number[-4:]}")
        self.status = "completed"

    def validate(self):
        return len(self.card_number) == 16

class NetBanking(Payment):

    # extra attribute = account_number
    def __init__(self, amount, account_number):
        super().__init__(amount)
        self.account_number = account_number

    def process(self):
        print(f"Processing amount ₹{self.amount} via NetBanking: *** *** **{self.account_number[-3:]}")
        self.status = "completed"

    def validate(self):
        return len(self.account_number) == 11

# PaymentProcessor - Composition

class PaymentProcessor:

    def __init__(self):
        self.payments = []     # empty list to store all payments

    def add_payment(self, payment):
        self.payments.append(payment)

    def process_all(self):        # if payment valid, process()
        for payment in self.payments:
            if payment.validate():
                payment.process()
                payment.receipt()
            else:
                print("Invalid payment details!")

    # Summary of all the payments and status
    def show_summary(self):
        for payment in self.payments:
            print(payment)
            print()

    # Compute total if status is completed
    def total_processed(self):       
        total = 0
        for payment in self.payments:
            if payment.status == "completed":
                total += payment.amount

        return total

# processor object 
processor = PaymentProcessor()

# add different payments
processor.add_payment(UPI(500, "stanley@upi"))
processor.add_payment(CreditCard(1000, "1234567890123456"))
processor.add_payment(NetBanking(750, "12345678901"))
processor.add_payment(UPI(300, "invalid-upi"))        # invalid
processor.add_payment(CreditCard(200, "123"))          # invalid

# use processor methods to test
processor.process_all()
print()
processor.show_summary()
print()
print(f"Total amount: {processor.total_processed()}")


        