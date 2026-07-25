class Animal:                               # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):                                  # base class
    def __init__(self, name, age, breed):
        super().__init__(name, age)          # super() for inherit all attribute from parent and specially add new attribute
        self.breed = breed                   # for child class

    def bark(self):
        print(f"{self.name} is barking!")

class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} is meowing")

dog1 = Dog("Bruno", 3, "Labrador")
cat1 = Cat("Whiskers", 5, "White")

print(dog1.name, dog1.age, dog1.breed)
print(cat1.name, cat1.age, cat1.color)
dog1.eat()                  # method inherited from parent
dog1.bark()
cat1.eat()
cat1.meow()




    

        
    