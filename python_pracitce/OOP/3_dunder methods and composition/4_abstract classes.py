# Abstract Classes - cannot be instantiated directly

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    pass             # doesn't implement speak()

# Test 1
animal = Animal("Generic", 5)

# Test 2
dog = Dog("Bruno", 3)
dog.speak()

# Test 3
cat = Cat("Whiskers", 5)

        
        