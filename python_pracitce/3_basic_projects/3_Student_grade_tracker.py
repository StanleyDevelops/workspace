# STUDENT GRADE TRACKER WITHOUT FILE HANDLING

def marks():
    maths = int(input("Enter your marks in maths: "))
    science = int(input("Enter your marks in science: "))
    english = int(input("Enter you marks in english "))
    store = {"maths": maths,
             "science": science,
             "english": english}
    
    return store 

student_db = {}
stay = True
while True:
     
    print("**************MENU****************")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Find Topper")
    print("5. Quit")

    try:
        choice = int(input("Enter your choice from Menu: "))
    except ValueError:
        print("Please enter correct option")
        continue

# Adding a student
    if choice == 1:
        name = input("Enter student name: ").strip()
        get_mark = marks()
        print(get_mark)
        student_db[name] = get_mark
        print(f"Marks added successfully.")

    elif choice == 2: 
        if not student_db:
            print("No students registered yet")
        else:
            for name, subjects in student_db.items():
                print(f"\nStudent: {name}")
                for subject, score in subjects.items():
                    print(f" - {subject.capitalize()}: {score}")

    elif choice == 3: 
        if not student_db:
            print(f"no student registered yet")
            continue

        for name, subjects in student_db.items():
                total_marks = sum(subjects.values())
                avg = total_marks/3

                print(f"\nStudent: {name}")
                print(f" Average marks: {avg:.2f}")

                if avg >=50:
                    print(" Status: Passed!")
                else:
                    print("Status: Failed")

    elif choice == 4:
        if not student_db:
            print("No students registered yet")
            continue

        topper_name = None
        highest_avg = -1

        for name, subjects in student_db.items():
            current_avg = sum(subjects.values()) / 3
            if current_avg > highest_avg:
                highest_avg = current_avg
                topper_name = name

        print(f"\n The topper is {topper_name} with an average of {highest_avg:.2f}")


    elif choice == 5:
        print("Closing Application.")
        break
                
        


    