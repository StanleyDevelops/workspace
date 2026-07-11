# __str__  and # __repr__    - only returns some str

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Grade: {self.grade}"
    
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
    
s1 = Student("Stanley", 19, "A")
s2 = Student("Mark", 90, "A+")

print(s1)                        # uses _str_
print(repr(s1))                  # uses _repr_

students = [s1,s2]               # uses _repr_
print(students)