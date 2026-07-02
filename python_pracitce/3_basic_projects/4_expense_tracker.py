# Expense Tracker to track daily expenses
expenses = [{"item": "lunch", "amount": 200, "category":"food"},
            {"item": "uber", "amount": 150, "category": "travel"},
            {"item": "jeans", "amount": 600, "category":"shopping"},
            {"item": "dinner", "amount": 400, "category": "food"}]


def add_expense():
    item = input("Enter an item: ")
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")

    store = {"item": item, "amount": amount, "category": category}

    return store


my_expenses =  []
stay = True 
while True:
    print("**********************MENU********************")
    print("-----------------------------------------------")
    print("1. Add an expense")
    print("2. View all expense")
    print("3. Show total amount spent")
    print("4. Show expense by category")
    print("5. Quit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter correct option")
        continue
     # add and expense
    if choice == 1:
        expenses = add_expense()
        my_expenses.append(expenses)
        print(my_expenses)
        print("Expenses Added!")

    # to show all the expenses
    elif choice == 2:
        if not my_expenses:
            print("There's no expense to Show!")
        else:
            for expense in my_expenses:
                print(expense)
    # to show total 
    elif choice == 3:
        if not my_expenses:
            print("Your expenses are empty!")
        else:
            total = 0
            for expense in my_expenses:
                total += expense['amount']
            print(f"Your Ultimate Total is: {total}")

     
    # to show the desired category expense 
    elif choice == 4:
        if not my_expenses:
            print("There's nothing Here my Man!")
        else:
            search_category = input("Enter the category to Find Total: ").lower().strip()
            totatl_category = 0
            find_any = False

            for expense in my_expenses:
                if expense.get('category') == search_category:
                    print(f"{expense['item']}: {expense['amount']}")
                    totatl_category += expense['amount']
                    found_any =True

            if found_any:
                print(f"Total - {search_category}: {totatl_category}")
            else: 
                print(f"No expense under {search_category}")

        # To find the Highest spent category

            highest_amount = -1
            highest_item = ""
            for expense in my_expenses:
                if expense['amount'] > highest_amount:
                    highest_amount = expense["amount"]
                    highest_item = expense['item']

            print(f"Highest spending of {highest_amount} on {highest_item}")

    # To exit the loop
    elif choice == 5:
        print("Exiting the App")
        print("See Ya!")
        stay = False
        break
        
        


