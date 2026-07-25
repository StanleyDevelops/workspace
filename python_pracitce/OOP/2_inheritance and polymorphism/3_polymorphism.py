# Adding describe() method to display polymorphism - many forms

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def speak(self):
        print(f"{self.name} makes a sound.")

    def describe(self):
        print(f"I am an animal named {self.name}")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):   # overrides Animal's speak
        print(f"{self.name} says: Woof!")

    def sleep(self):
        print(f"{self.name} crashes on the couch")

    def describe(self):
        print(f"I am a {self.breed} Dog named {self.name}") 

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):   # overrides Animal's speak
        print(f"{self.name} says: Meow!")

    def eat(self):
        super().eat()
        print(f"{self.name} licks paws after eating.")

    def describe(self):
        print(f"I am a {self.color} Cat named {self.name}")

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def sleep(self):
        super().sleep()
        print(f"{self.name} tucks head under wing.")  

    def describe(self):
        print(f"I am a bird named {self.name} with a wingspan of {self.wingspan}cm")  

 
animals = [Animal("Default", 12),
           Dog("Bruno", 9, "BullDog"),
           Cat("Whiskers", 15, "grey"),
           Bird("D. Mellow", 9, 30)]

# same method name, different behaviour according to object
for animal in animals:
    animal.describe()
