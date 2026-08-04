# Student grade system to demo @property decorator

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade   # private attribute

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            print("Grade must be betwenn 0 and 100!")
        else:
            self.__grade = value

    # defines what happens when you delete object.attribute
    @grade.deleter
    def grade(self):
        print(f"Deleting {self.name}'s grade.")
        del self.__grade


# Testing object
s1 = Student("Stanley", 85)
print(s1.grade)        # getter
s1.grade = 95          # setter
print(s1.grade)
s1.grade = 150         # rejected value
del s1.grade           # deleter 

        