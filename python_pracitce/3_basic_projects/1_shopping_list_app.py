# Simple shopping list app

stay = True
shop_list = []
while stay:
     # Menu shown in a loop   
    print("--------Menu--------")
    print("1. View items ")
    print("2. Add items ")
    print("3. Remove item ")
    try:    # Taking input
        choice = int(input("Enter your choice from Menu: "))
    except ValueError:
        print("Please Enter correct option.")
        print()
        continue

    # To handle if the list is empty already
    if choice == 1:
        if len(shop_list) == 0:
            print("The list is empty")
            print()
            continue

        else:  # prints the list items
            print("The list conatins: ")
            for i in range(0,len(shop_list)):
                print(f"{i+1}. {shop_list[i]}")

    # To add items
    elif choice == 2:
            more = True
            while more:
    
                add_item = str(input("Enter an item to add: ")).lower()
        
                shop_list.append(add_item)
                print(f"{add_item} added to the list.")

                
                add_more = input("Add more items? (y/n): ").lower() 
                if add_more != 'y':
                    more = False
            
     # removing an item
    elif choice  == 3:

        remove_item = input("Enter item to remove: ").lower()   

        if remove_item in shop_list:
            shop_list.remove(remove_item)
            print("Item removed successfully!!")
            print()
        else:
            print("The item doesn't exist in the list.")
    
    # to exit from the loop
    exit = str(input("Do you want to exit? (y/n): ")).lower()
    if exit == 'y':
        stay = False



