# Employee Record System
from collections import namedtuple

Employee = namedtuple("Employee", ['id', 'name', 'salary'])

employees = []

def add_employee():
    try:
        emp_id = input("Enter Employee Id: ")
        name = input("enter Employee name: ")
        salary = float(input("Enter Employee salary: "))

        employee = Employee(emp_id, name, salary)

        return employee
    
    except ValueError:
        print("Invalid salary!")
        return None
    
while True:
    print("===============Employee Record System=============")
    print("1. Add Employee")
    print("2. Show All Employee")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        employee = add_employee()

        if employee:
            employees.append(employee)
            print(f"{employee.name} added. ")

    elif choice == 2:
        if not employees:
            print(f"No employee records.")
        else:
            print("Employee Records:")
            for emp in employees:
                print(emp._asdict())

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid Input!")



