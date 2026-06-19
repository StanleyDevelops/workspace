# Browser History Simulator

from collections import deque

back_list = deque([])
forward_list = deque([])
current_page = None

while True:
    print("*************Browsing History Simulator*************")
    print("-------------MENU------------")
    print("1. Visit a new Page.")
    print("2. Go back.")
    print("3. Go forward.")
    print("4. Exit.")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please choose valid option.")

    if choice == 1:
        new_page = input("Enter a new page: ")

        if current_page is not None:
            back_list.append(current_page)

        current_page = new_page
        forward_list.clear()

        print(f"Current page: {current_page}")
        

    elif choice == 2:
        if not back_list:
            print("No Previous page")
        else:
            forward_list.append(current_page)
            current_page=back_list.pop()

            print(f"Current Page: {current_page}")
        

    elif choice == 3:
        if not forward_list:
            print("No next page!")
        else:
            back_list.append(current_page)
            current_page = forward_list.pop()         
            print(f"Current page: {current_page}")

    elif choice == 4:
        print("EXITING...")
        break

    else:
        print("Inavlid Choice!!")
    
    print("Back History  :", list(back_list))
    print("Forward History:   ", list(forward_list))
            
        



