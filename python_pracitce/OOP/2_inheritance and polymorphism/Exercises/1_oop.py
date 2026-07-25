# Building Animal Parent Class with sub-classes
# demo of super()

class Animal:
            # The parent with default attributes for all the child
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):

    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

    def fetch(self):
        print(f"{self.name}({self.breed}) is fetching the stick")

class Cat(Animal):

    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} is meowing.")

class Bird(Animal):
    
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying.")

dog1 = Dog("Bruno", 12, "Retriever")
cat1 = Cat("Jellow", 3, "Smoke white")
bird1 = Bird("Marlow", 8, "30.5cm")

# test the dog object
print(dog1.name,dog1.age,dog1.breed)
dog1.bark()                   # from child itself
dog1.sleep()                  # from parent
dog1.fetch()

print()

# test the cat object
print(cat1.name, cat1.age, cat1.color)
cat1.meow()

print()

# testing bird object
print(bird1.name, bird1.age, bird1.wingspan)
bird1.fly()





        