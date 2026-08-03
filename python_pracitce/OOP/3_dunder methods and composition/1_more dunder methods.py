# Dunder Methods to define built-in types
class Cart:

    def  __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    

cart = Cart(["apple", "banana", "cherry"])
print(len(cart))

# __add__ method
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):          # defining what add (+) does 
        return self.balance + other.balance
    
acc1 = BankAccount("Stanley", 500)
acc2 = BankAccount("Rahul", 300)

print(acc1 + acc2)
        
# __eq__ method
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __eq__(self, other):
        return self.balance == other.balance

acc1 = BankAccount("Master", 100)
acc2 = BankAccount("Commander", 200)
print(acc1 == acc1)        
        
# __lt__ - less than method 
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def __lt__(self, other):
        return self.balance < other.balance

acc3 = BankAccount("Matthew", 100)
acc4 = BankAccount("Mark", 200)
print(acc3 > acc4)        
        


        
        