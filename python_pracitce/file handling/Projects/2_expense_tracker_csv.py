import csv
FILE_NAME = "expenses.csv"

def add_expense():
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category,amount])
    
    print("Expense Saved with Success!!")

def show_expense():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            
            print("\nEXPENSES:")
            for row in reader:
                print(f"{row[0]}: {row[1]}")
    except FileNotFoundError:
        print("There is not Expense record.")

def show_total():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            total = 0
            for row in reader:
                total += int(row[1])

        print("Total Amount = ", total)
    except Exception as e:
        print(f"{e}")

while True:
    print("----------------MENU--------------")
    print("1. Add expense")
    print("2. Show all Expenses")
    print("3. Show Total Amount Spent")
    print("4. Exit")

    try:
        choice = int(input("Enter Your choice: "))
    except ValueError:
        print("Please enter valid choice!")

    if choice == 1:
        add_expense()

    elif choice == 2:
        show_expense()

    elif choice == 3:
        show_total()

    elif choice == 4:
        print("Exiting...")
        break

    