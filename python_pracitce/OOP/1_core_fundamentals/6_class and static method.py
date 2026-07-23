
# Class and static method    

class BankAccount:

    total_accounts = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance   
        BankAccount.total_accounts += 1

    @classmethod  # operates directly on class
    def get_total_accounts(cls):   # needs cls
        return f"Total Account: {cls.total_accounts}"
     
    @staticmethod   # regular function inside class
    def validate_amount(amount):
        return amount > 0
    
    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.__balance}"
    
    def __repr__(self):
        return f"BankAccount(Owner = {self.owner}, Balance = {self.__balance})"
    
    def deposit(self,amount):
        if not BankAccount.validate_amount(amount):  # if amount is NOT valid
            print("Invalid amount!")
            return
        self.__balance += amount
        print(f"{amount} Deposited in account.")

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):  # if amount is NOT valid
            print("Invalid amount!")
            return
        if amount > self.__balance:
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


acc1 = BankAccount("Stanley")
acc2 = BankAccount("Rahul", 500)
acc3  = BankAccount("Priya", 1000)

print(BankAccount.get_total_accounts())
acc1.deposit(100)
acc1.deposit(-50)
print(acc1.get_balance())
         