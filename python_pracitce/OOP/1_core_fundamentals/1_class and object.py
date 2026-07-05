# self - object reference to itself
class students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

s1 = students("Stanley", 19, "A+")
print(s1.age)
print(s1.grade, s1.name)

# 

class students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hello, My name is {self.name}, I'm {self.age} Y/O, grade is {self.grade}")

    def show_grade(self):
        print(f"{self.name}'s garde is {self.grade}")

s1 = students("Niral", 13, "A")
s2 = students("Kerketta", 89, "D+")

s1.introduce()
s2.introduce()
s2.show_grade()