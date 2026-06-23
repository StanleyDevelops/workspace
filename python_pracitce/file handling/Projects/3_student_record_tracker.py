# STUDENT RECORD TRACKER
import json
file_name = "students.json"


def load_students():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_all_students(student_list):
    with open(file_name, "w") as file:
        json.dump(student_list, file, indent=4)
   
students = load_students()

while True:
    print("1. Add students")
    print("2. View All students")
    print("3. Search student by Name:")
    print("4. Delete a student by Name: ")
    print("5. Exit")

    try: 
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter valid option!")
        continue

    if choice == 1:
        name = input("Enter name of the student: ")
        age = int(input("Enter age: "))
        branch = input("Enter Branch: ")

        students.append({"name": name,"age": age, "branch": branch})
        save_all_students(students)
        print("Student Added with Success!")

    elif choice == 2:
        for student in students:
            print(f"NAME: {student['name']} |  AGE: {student['age']} | BRANCH: {student['branch']}")

    elif choice == 3:
        student_name = input("Enter name of student: ")
        found = False
        for student in students:
            if student_name.lower() == student['name'].lower():
                print(f"Student Name: {student['name']}| Age: {student['age']} | Branch: {student['branch']}")
                found = True
                break
        if not found: 
            print(f"Cannot Find Student {student_name}")

    elif choice == 4:
        student_name = input("Enter name of student: ")
        orginal_length = len(students)

        students = [s for s in students if s['name'].lower() != student_name.lower()]

        if len(students) < orginal_length:   # it means we found a match
            save_all_students(students)
            print(f"{student_name} deleted with success!!")
        else:
            print(f"{student_name} not found!!")
   
    elif choice == 5:
        print("Exiting...")
        break