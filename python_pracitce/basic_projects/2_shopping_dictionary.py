# CLI Shoppping app but with dictionary

shop_dictionary = {}
stay = True
while stay:
    # Making the menu that shows within loop
    print("*************Shopping__Dictionary**************")
    print("----------------------------------------------")
    print("1. View items")
    print("2. Add items")
    print("3. Remove items")

    # taking user choice from menu
    try:
        user_choice = int(input("Enter your option: "))
    except ValueError:
        print("Please enter correct option!")
        continue
    
    if user_choice == 1:
        # handle if the is dictionary empty
        if not shop_dictionary:  
            print("The Dictionary is empty!")    # elegent pythonic way
        else:
            print("The items are: ")
            for item, quantity in shop_dictionary.items():
                print(f"{item.capitalize()}: {quantity}")

    elif user_choice == 2: 
        # input to add in a dictionary
        add_item = input("Enter an item to add: ").lower().strip()
        try:
            qty = int(input("Enter the quantity: "))
        except ValueError:
            print("Setting the quantity to 1")
            qty = 1

        # the dictionary logic
        shop_dictionary[add_item] = shop_dictionary.get(add_item, 0) + qty
        print(f"Updated {add_item} to quantity - {shop_dictionary[add_item]}")

    # To Remove item
    elif user_choice == 3:
        remove_item = input("Enter the item to remove: ")

        if remove_item in shop_dictionary:
            shop_dictionary.pop(remove_item)
            print(f"{remove_item} removed successfully")
        else:
            print("The item doesn't exist in the dictionary")

    user_exit = input("Do you want to exit?(y/n):").lower()
    if user_exit == 'y':
        stay = False

    print("GoodBye!! Happy Shopping!!")

