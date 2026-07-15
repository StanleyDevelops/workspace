''' # building a car class
class Car:

    # class attribute initialize
    total_cars = 0
    
    # adding different attributes
    def __init__(self,make,model,year,speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        Car.total_cars += 1

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, Speed: {self.speed}"
    
    def accelerate(self,amount):
        self.speed += amount
        print(f"Car accelerated by {amount}m/s")

    def brake(self,amount):

        # validating negative amount
        if amount<0:
                print("Speed cannot be negative!")
                
        else:  
            self.speed = max(0,self.speed - amount)   # take whichever is bigger: 0 or the result
            print(f"Car decelerated by {amount}m/s")
            if self.speed == 0:
                print("Car has stopped!")
        

car1 = Car("Toyota", "Corolla", 2026)
car1.accelerate(10)
car1.brake(10)
print(Car.total_cars)
print(car1)   '''

# building a bankaccount class
class BankAccount:
     
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount < 0:
            print("Cannot deposit negative amount!")
        else:
            self.balance += amount
            print(f"₹{amount} deposited to account.")

    def withdraw(self,amount):

        # validate negative amount
        if amount < 0:
            print(f"Withdraw amount cannot be negative!")
        
        # reject withdraw if amount exceed balance
        elif amount > self.balance:
            print(f"Insufficient Funds!")
        else:
            self.balance -= amount
            print(f"₹{amount} Deducted from account.")

    def get_balance(self):
        return f"Current balance = ₹{self.balance}"

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: {self.balance}"
    
    def __repr__(self):
        return f"BankAccount(Owner = {self.owner}, Balance = {self.balance})"
    

acc1 = BankAccount("Stanley")
print(acc1)
acc1.deposit(100)
acc1.get_balance()
acc1.withdraw(80)
acc1.get_balance()
acc1.withdraw(20)
acc1.get_balance()
print(repr(acc1))



