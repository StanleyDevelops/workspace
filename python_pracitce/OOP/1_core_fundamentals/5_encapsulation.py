# Encapsulation is a method to restrict direct access to object's data
# controlling how it's modified

class BankAccount:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance     # now its's private

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"
    
    def __repr__(self):
        return f"BankAccount(Owner = {self.owner}, Balance = {self.__balance})"
    
    def deposit(self,amount):
        if amount < 0:
            print("Amount cannot be negative!")
        else:
            self.__balance += amount
            print(f"{amount} Deposited in account.")

    def withdraw(self, amount):
        if amount < 0:
            print(f"Negative amount not allowed!")
        elif amount > self.__balance:
            print(f"Insufficient Funds")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn from account.")

    # Notion of getter and setter

    def get_balance(self):
        return self.__balance    #  returns the value - getter
    
    def set_balance(self,amount):   # write private data with validation
        if amount < 0 :
            print(f"Negative amount not allowed!")
        else:
            self.__balance = amount

acc1 = BankAccount("Amrit")      
acc1.deposit(500)
print(acc1.get_balance())  
acc1.set_balance(-100)
acc1.set_balance(1000)
print(acc1.get_balance())
     
