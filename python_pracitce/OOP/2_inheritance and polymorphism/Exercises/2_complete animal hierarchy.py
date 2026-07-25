# Complete Animal hierarchy from scratch

class Animal:                 # the Parent

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):                   # return when an object is called
        return f"Name: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        return f"Animal(Name: {self.name}, Age: {self.age})"   # for developers, for complete info of the class 

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def speak(self):
        print(f"{self.name} is making a sound.")

    def describe(self):
        print(f"Hello! I'm {self.name}, {self.age} years old.")

class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name}, a {self.breed} is barking.")

    def eat(self):
        super().eat()
        print(f"{self.name} wags his tail after eating.")

    def fetch(self):
        print(f"{self.name} is fetching a stick.")

class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} is meowing.")

    def sleep(self):
        super().sleep()
        print(f"{self.name} is stretching after sleeping.")

    def purr(self):
        print(f"{self.name} is purring.")

class Bird(Animal):

    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def speak(self):
        print(f"{self.name} is chirruping.")

    def fly(self):
        print(f"{self.name} is flying up high.")


animals = [
    Dog("Bruno", 3, "Labrador"),
    Cat("Whiskers", 5, "White"),
    Bird("Marlow", 8, 30.5)
]

print(repr(animals))     # repr is used when a lis is passed

for animal in animals:
    animal.speak()
    animal.describe()
    print(animal)    # return str method
    print() 



animals[0].eat()
animals[0].fetch()   # new method in child class
print()

animals[1].sleep()   # overriding and extending
animals[1].purr()
print()

animals[2].speak()
animals[2].fly()
print()


    

    

        