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

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):   # overrides Animal's speak
        print(f"{self.name} says: Woof!")

    def sleep(self):
        print(f"{self.name} crashes on the couch")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):   # overrides Animal's speak
        print(f"{self.name} says: Meow!")

    def eat(self):
        super().eat()
        print(f"{self.name} licks paws after eating.")

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def sleep(self):
        super().sleep()
        print(f"{self.name} tucks head under wing.")    

animal1 = Animal("Generic Animal", 5)
dog1 = Dog("Bruno", 3, "Labrador")
cat1 = Cat("Whiskers", 5, "White")
bird1 = Bird("Marlow", 8, 30.5)

animal1.speak()
dog1.sleep()
cat1.eat()
bird1.sleep()