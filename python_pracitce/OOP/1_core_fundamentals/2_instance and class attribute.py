# instance and class attribute

class students:
    school = "Good Samaritan School"

    def __init__(self,name,age):
        self.name = name   # instance attribute - unique per element
        self.age = age

s1 = students("Matthew", 67)
s2 = students("Mark", 90)
print(s2.school)
print(s1.school)     # both object share class attribute


# students.school = "The JayPee"
# print(s1.school)

s1.school = "IIT Bombay"        # new instance attribute shadowing class one
print(s1.school)
print(s2.school)
print(students.school)
