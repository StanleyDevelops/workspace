# ShoppingCart class to demo dunder methods

class ShoppingCart:

    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def __str__(self):
        return f"{self.owner}'s cart: {len(self.items)} items"
    
    def __repr__(self):
        return f"ShoppingCart(owner = {self.owner}, items = {self.items})"    

    def __len__(self):
        return len(self.items)
    
    def __add__(self, other):
        total = 0
        for i in self.items:
            total += i["price"]
        
        for j in other.items:
            total += j["price"]

        return f"Total Price: {total}"
    
    def __eq__(self, other):
        return len(self.items) == len(other.items)

    def __lt__(self, other):
        return len(self.items) < len(other.items)
    
cart1 = ShoppingCart("Stanley", [
    {"name": "apple", "price": 30},
    {"name": "milk", "price": 50},
    {"name": "bread", "price": 40}
])

cart2 = ShoppingCart("Rahul", [
    {"name": "rice", "price": 100},
    {"name": "oil", "price": 150},
    
])

print(len(cart1))
print(cart1 + cart2)
print(cart1 == cart2)
print(cart1 < cart2)
print(cart1)
print(repr(cart2))
    


            


        
