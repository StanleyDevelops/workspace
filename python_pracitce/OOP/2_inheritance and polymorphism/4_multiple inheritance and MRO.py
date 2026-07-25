# Multiple inheritance - inherits from multiple parents

class Father:
    def skill(self):
        print("Cooking")

class Mother:

    def skill(self):
        print("Painting")

class Child(Father,Mother):    # inherits both
    pass

c = Child()
c.skill()    # only prints Father's method because of MRO
print(Child.__mro__)                 # multiple resolution order

# Mixins - Where multiple inheritance is used

class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)    # self.__dict__["owner"] = "Stanley"

class LogMixin:
    def log(self):
        print(f"[LOG] {self.__class__.__name__} object created")

class BankAccount(JsonMixin, LogMixin):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Stanley", 500)
acc1.log()
print(acc1.to_json())