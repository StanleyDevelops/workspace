# Using @property to demo getter and setters

class BankAccount:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Owner: {self.owner} || Balance: {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Invalid amount!")
        else:
            self.__balance = value

acc1 = BankAccount("Stanley", 500)
print(acc1.balance)     # should print 500
acc1.balance = 1000     # should work
acc1.balance = -100     # should reject
print(acc1.balance)     # should print 1000

    
        