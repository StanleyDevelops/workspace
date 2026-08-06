# Complete Banking System using OOP

from abc import ABC, abstractmethod

# abstract base
class Account(ABC):

    # base account constructor
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance            # protected attribute
        self.transaction_history = []      # to store amount transfer history

    # getter method
    @property
    def balance(self):
        return self._balance
        
    # add money to bank account
    def deposit(self, amount):
        if amount < 0:
            print("Please enter valid amount!")
        else:
            self._balance += amount
            print(f"₹{amount} deposited to Account.")

            # add transaction record
            self.transaction_history.append({"type": "deposit",
                                             "amount": amount,
                                             "balance_after": self._balance}) 

    
    # abstract method - different per account
    @abstractmethod               
    def withdraw(self, amount):
        pass                       # abstract method should return pass only

    # to print when an object is called
    def __str__(self):
        return f"Account Number: {self.account_number} || Owner: {self.owner} || Balance: {self.balance}"

    def __repr__(self):
        return f"Account((Account Number: {self.account_number} || Owner: {self.owner} || Balance: {self.balance}))"    

    # to display all the transactions
    def show_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        for t in self.transaction_history:
            print(f"{t['type'].upper()} || ₹{t["amount"]} || Balance after: {t["balance_after"]}")

    # method to transfer from one account to another
    def transfer(self, amount, target_account):
            previous_balance = self._balance
            self.withdraw(amount)   # uses correct validation per account type
            
            # only deposit to target if withdrawal actually succeeded
            if self._balance < previous_balance:
                target_account._balance += amount    # directly update, skip deposit() recording
                # record transfer in history
                self.transaction_history.append({
                    "type": "transfer_out",
                    "amount": amount,
                    "balance_after": self._balance
                })
                target_account.transaction_history.append({
                    "type": "transfer_in",
                    "amount": amount,
                    "balance_after": target_account._balance
                })
                print(f"₹{amount} transferred to {target_account.owner}.")

 
class SavingsAccount(Account):

    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = float(interest_rate)

    # extract money 
    def withdraw(self, amount):
        if amount < 0:
            return f"Please enter valid amount!"
        if self._balance - amount < 500:
            print(f"Withdrawal denied! Balance cannot drop below 500.")
            return
        else:
            self._balance -= amount 
        print(f"₹{amount} withdrawn successfully.")
        self.transaction_history.append({"type": "withdraw",
                                        "amount": amount,
                                        "balance_after": self._balance}) 

    def add_interest(self):             # no rate parameter needed
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest of ₹{interest:.2f} added to {self.owner}'s account.")


class CurrentAccount(Account):

    # A current account (used by businesses) allows you to withdraw
    # more than your balance up to a certain limit. That 
    # negative amount is called an overdraft.

    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            print(f"Please enter positive amount!")
            return
        if self.balance - amount < -self.overdraft_limit:
            print("Overdraft limit exceeded!")
            return
        else:
            self._balance -= amount
        print(f"₹{amount} withdrawn.")
        self.transaction_history.append({"type": "withdraw",
                                                "amount": amount,
                                                "balance_after": self._balance}) 

class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts =  []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account added to {self.name}.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:   # if account numbers matches, return account
                return account
        else:
            print(f"Incorrect account number! Try again.")
            return None            # exit after checking account number

    def total_deposits(self):
        total = 0
        for account in self.accounts:
            total += account.balance   
        print(f"Total deposits: ₹{total}")

    def show_all_accounts(self):
        print(f"------ACCOUNTS-----")
        for account in self.accounts:
            print(account)

    # Adding show rich account and apply interest to all features

    def show_rich_accounts(self, threshold):   
        # show all accounts with balance above threshold

        for account in self.accounts:
            if account.balance > threshold:
                print(f"Owner: {account.owner} || Balance: {account.balance}")

    def apply_interest_all(self):

        total_acc_interest = 0
        for account in self.accounts:
            if isinstance(account, SavingsAccount):  # Returns True or False
                account.add_interest()
                total_acc_interest += 1

        print(f"The Total Account Applied Interest to: {total_acc_interest}")

        

# testing account objects
'''
sav = SavingsAccount("Stanley", "SAV001", 2000, interest_rate=0.05)
cur = CurrentAccount("Rahul", "CUR001", 1000, overdraft_limit=500)

# testing savingsaccount object
sav.deposit(500)
print(sav.balance)
sav.withdraw(1800)   # works
sav.withdraw(1500)   # rejects - would go below 500 minimum
print(sav.balance)


cur.deposit(200)
print(cur.balance)
cur.withdraw(1500)   # works - within overdraft limit
cur.withdraw(500)    # rejects - exceeds overdraft limit
print(cur.balance)  '''

# Test Bank class with composition
'''
bank = Bank("Stanley's Bank")

sav = SavingsAccount("SAV001", "Stanley", 2000, interest_rate=0.05)
cur = CurrentAccount("CUR001", "Rahul", 1000, overdraft_limit=500)

bank.add_account(sav)
bank.add_account(cur)

bank.show_all_accounts()
print()
bank.total_deposits()
print()

# matches account
found = bank.find_account("SAV001")
print(found)

# account doesn't match
not_found = bank.find_account("XYZ999")  '''


# Testing transfer() and transactions history methods
'''
bank = Bank("Stanley's Bank")
sav = SavingsAccount("SAV001", "Stanley", 2000, interest_rate=0.05)
cur = CurrentAccount("CUR001", "Rahul", 1000, overdraft_limit=500)

bank.add_account(sav)
bank.add_account(cur)

sav.deposit(500)
sav.withdraw(300)
sav.transfer(200, cur)
cur.withdraw(100)

print("\n--- Stanley's History ---")
sav.show_history()

print("\n--- Rahul's History ---")
cur.show_history()  '''

# Testing rich accounts and apply interest all methods

bank = Bank("Stanley's Bank")
sav1 = SavingsAccount("SAV001", "Stanley", 2000, interest_rate=0.05)
sav2 = SavingsAccount("SAV002", "Priya", 5000, interest_rate=0.08)
cur = CurrentAccount("CUR001", "Rahul", 1000, overdraft_limit=500)

bank.add_account(sav1)
bank.add_account(sav2)
bank.add_account(cur)

bank.show_rich_accounts(1500)
print()
bank.apply_interest_all()
print()
bank.show_all_accounts()