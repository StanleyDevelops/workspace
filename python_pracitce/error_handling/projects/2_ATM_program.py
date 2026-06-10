# ATM Program
# Ultimate exception handling 

class InsuficientBalanceError(Exception):
    pass

class AmountError(Exception):
    pass

balance = 1000
stay = True
while stay:
    print("======================MENU==================")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try: 
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter valid option!")
        continue

    if choice == 1:
            print(f"The Current Balance: {balance}")

    elif choice == 2:
        try:
            deposit_amount = int(input("Enter amount to Deposit"))
           
            if deposit_amount <= 0:
                raise AmountError("The Amount should be Greater than 0")
        except ValueError:
            print("Please enter an Integer amount")
        except AmountError as e:
            print(f"Invalid input: {e}")
        else: 
            balance += deposit_amount
        finally:
            print(f"The Current Balance: {balance}")
        
    elif choice == 3:
        try:
            withdraw_amount = int(input("Enter amount to withdraw: "))

            if withdraw_amount <=0:
                raise AmountError("The Amount should be greater than Zero!")
            if withdraw_amount > balance:
                raise InsuficientBalanceError("The Withdraw Cannot Exceed Balance!")
            
        except ValueError:
            print("Please enter Integer input!")
        except AmountError as e:
             print(f"Invalid input: {e}")
        except InsuficientBalanceError as f:
            print(f"Error: {f}")
        else:
            balance -= withdraw_amount
        finally:
            print(f"The Current Balance: {balance}")

    elif choice == 4:
        print("Happy ATM.")
        print("GoodBye!")
        print("Exiting...")
        stay = False
            

