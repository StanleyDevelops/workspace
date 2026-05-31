# Find student with highest marks
student ={
 "Ram": 80,
 "Shyam": 92,
 "Mohan": 75
}
highest_student =  max(student, key = student.get)

print(f"The student with highest marks is {highest_student} : {student[highest_student]}")

# Manual Method
student ={
 "Ram": 88,
 "Shyam": 91,
 "Mohan": 70
}

highest_student = None     # no track initially
highest_marks = float('-inf')

for name, marks in student.items():
    if student[name] > highest_marks:  # if someone found worthy, starts tracking it
        highest_marks = student[name]
        highest_student = name

print(f"{highest_student} has highest of {highest_marks}")