# Product Inventory System

class Product:
    store_name = "TechStore"

    def __init__(self, name, price, stock):
        self.__name = name    # private attributes
        self.__price = price
        self.__stock = stock

    def __str__(self):
        return f"Product: {self.__name} | Price: {self.__price} | Stock: {self.__stock}"
        
    def __repr__(self):
        return f"Product({self.__name}, {self.__price}, {self.__stock})"

    # Pythonic way to use setters and setters
    @property
    def price(self):          # getter method
         return self.__price
    
    @price.setter
    def price(self, new_price):    # setter method
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = new_price

    def sell(self, quantity):
        if quantity > self.__stock:
            raise ValueError("Not enough stock available.")
        self.__stock -= quantity
        return f"Sold {quantity} units of {self.__name}. Remaining stock: {self.__stock}"
    
pro1 = Product("laptop", 90000, 5)
pro1.price = 85000   # runs @price.setter 
print(f"Updated Price: {pro1.price}")     # getter method

print(pro1.sell(4))
print(str(pro1))
print(repr(pro1))
