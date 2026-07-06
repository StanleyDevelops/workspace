# Add a class attribute total_students that 
# tracks how many Student objects have been created.
# Every time __init__ runs, it should increment by 1.

class students:
     
    # initializing the class attribute
    total_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        students.total_student += 1

s1 = students("Stanley", 10)
s2 = students("Jesus", 33)
s3 = students("Paul", 89)
print(students.total_student)
print(s1)
