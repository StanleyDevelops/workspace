while True:
    print("1. Add note")
    print("2. View all notes")
    print("3. Exit")

    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Please enter valid option")
        continue

    if choice == 1:
        add_note = input("Enter a note: ")
        with open("notes.txt", "a") as file:
            file.write(f"{add_note}\n")
        print("Note added successfully")

    elif choice == 2:
        try: 
            with open("notes.txt", "r") as file:
                print("NOTES: ")
                for i,item in enumerate(file):
                    print(f"{i+1}: {item}")
        except FileNotFoundError:
            print("No Notes Found")

    elif choice == 3:
        print("Exiting..")
        break
