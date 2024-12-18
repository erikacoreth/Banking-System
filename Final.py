import random


class Account:
    def __init__(self, firstname, lastname, ssn):
        self.account_number = random.randint(10000000, 99999999) #8 digit number
        self.first = firstname
        self.last = lastname
        self.set_ssn(ssn)
        self.pin = f"{random.randint(0, 9999):04}" #4-digit PIN (may start with 0)
        self.balance = 0 #Balance in cents for precision

    #getter and setter for owners first name
    def get_firstname(self):
        return self.first
    def set_firstname(self, firstname):
        if not firstname.strip():
            raise ValueError("First name cannot be empty.") #checks to make sure its not empty
        self.firstname = firstname

    #getter and setter for owners last name
    def get_lastname(self):
        return self.last

    def set_lastname(self, lastname):
        if not lastname.strip():
            raise ValueError("Last name cannot be empty.") #checks to make sure its not empty
        self.last = lastname

    #getter and setter for ssn
    def get_ssn(self):
        return self.ssn

    def set_ssn(self, ssn):
        if len(ssn) != 9 or not ssn.isdigit(): #checks to make sure ssn is 9 digits and if its in fact, numbers
            raise ValueError("SSN must be a 9-digit number.")
        self.ssn = ssn

    #getter and setter for PIN
    def get_pin(self):
        return self.pin

    def set_pin(self, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit(): #makes sure its a 4 digit number
            raise ValueError("PIN must be a 4-digit number.")
        self.pin = new_pin

    #getter and setter for balance
    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        if new_balance < 0: #has to be greater than 0
            raise ValueError("Balance cannot be negative.")
        self.balance = new_balance

    def deposit(self, amount): #makes sure deposit is a positive number
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount): #makes sure you withdraw a positive number
        #also makes sure you have enough money in your account to withdraw the amount you want
        if amount <= 0:
            raise ValueError("Withdrawl amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def isValidPIN(self, pin):
        return self.pin == pin
    #if pin matches, returns True, if pin does not match, returns false

    def to_string(self):
        return (f"Account Number: {self.account_number}\n"
                f"Owner Name: {self.get_firstname()} {self.get_lastname()}\n"
                f"Social Security Number: {self.get_ssn()}\n"
                f"PIN: {self.get_pin()}\n"
                f"Balance: ${self.get_balance() / 100:.2f}") # /100 converst from dollars to cents
                    #.2f will round number to 2 decimals places

class Bank:
    MAX_ACCOUNTS = 100 #max number of accounts supported by the bank

    def __init__(self):
        #initialize the accounts list with None to represent 100 empty slots that accounts could be in
        self.accounts = [None] * self.MAX_ACCOUNTS

    def addaccounttobank(self, account):
        #return true if it adds, false if bank is full
        for i in range(len(self.accounts)):
            if self.accounts[i] is None: #look for the first empty slot
                self.accounts[i] = account
                print(f"Account {account.account_number} added successfully.")
                return True
        print("No more accounts available.") #Bank is full
        return False

    def removeAccountFromBank(self, account):
        #remove account from the bank based on the account object
        for i in range(len(self.accounts)):
            if self.accounts[i] is not None and self.accounts[i].account_number == account.account_number:
                self.accounts[i] = None # mark this slot as empty
                print(f"Account {account.account_number} removd.")
                return True
        print(f"Account {account.account_number} not found.")
        return False

    def findAccount(self, account_number):
        #find and return an account by its #
        #returns the account object if found, or None if not
        for account in self.accounts:
            if account is not None and account.account_number == account_number:
                return account
        return None #account not found

    def addMonthlyInterest(self, annual_interest_rate):
        #add monthly interest to all accounts in the bank.
        monthly_rate = annual_interest_rate / 12 / 100 #convert to decimal and monthly rate
        for account in self.accounts:
            if account is not None:
                interest = int(account.balance * monthly_rate) #calculate monthly interest in cents
                account.deposit(interest)
                print(f"Added ${interest / 100:.2f} interest to account {account.account_number}.")

    def listAllAccounts(self):
        accounts_found = False
        print("Listing all accounts:")
        for account in self.accounts:
            if account is not None:
                print(f"Account Number: {account.account_number}")
                accounts_found = True
        if not accounts_found:
            print("No accounts available.")


class CoinCollector:
    @staticmethod
    #parsese a string of coin characters and calculates the total value in cents.
    #args: coins(str): a string representing a set of coins
    #returns:int: the total value of the coins in cents
    def parseChange(coins):
        #mapping of coin characters to their values in cents
        coin_values= {
            'P': 1, #penny
            'N': 5, #Nickel
            'D': 10, #dime
            'Q': 25, #quarter
            'H': 50, #halfdollar
            'W': 100, #whole dollar
        }

        #initizlize total value
        total = 0

        #iterate through each character in the string
        for char in coins:
            #check if the character is a valid coin
            if char in coin_values:
                total += coin_values[char]
            else:
                raise ValueError(f"Invalid coin character: {char}")
        return total

class BankUtility:
    @staticmethod
    #prompts user number a non-empty string is provided
    def promptUserForString(prompt):
        while True:
            user_input = input(prompt)
            if len(user_input.strip()) > 0:
                return user_input
            else:
                print("Input cannot be empty. Please try again.")

    #prompts user until a positive number is entered
    #also uses isNumeric to make sure its a number before defining if it is positive
    @staticmethod
    def promptUserForPositiveNumber(prompt):
        while True:
            user_input = input(prompt)
            if BankUtility.isNumeric(user_input):
                number = int(user_input)
                if number > 0:
                    return number
                else:
                    print("Amount cannot be negative or zero. try again.")
            else:
                print("Invalid input. Please enter a numeric value.")

    #generates a random int within a range
    @staticmethod
    def generateRandomInteger(min, max):
        try:
            return random.randint(min, max)
        except ValueError:
            print("Invalid range. Ensure min is less than or equal to max.")
            return None

    #converts dollar amount into cents as an integer
    @staticmethod
    def convertFromDollarsToCents(amount):
        try:
            return int(amount * 100)
        except (TypeError, ValueError):
            print("Invalid input. Please enter a valid dollar amount.")
            return 0

    #checks if numbertocheck contains only digits
    @staticmethod
    def isNumeric(numberToCheck):
        try:
            if str(numberToCheck).isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

class BankManager:
    def main(self):
        #bank object
        bank = Bank()

        #Display the main menu and process user input
        while True:
            print("\nBank Menu:")
            print("1. Add Account")
            print("2. Remove Account")
            print("3. Find Account")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. Show Balance")
            print("7. Add Monthly Interest")
            print("8. List All Accounts")
            print("9. Close Account")
            print("10. Display Account Details")
            print("11. Exit")

            #get user choice
            choice = input("Enter your choice (1-11): ")

            #Exit if the user chooses 11
            if choice == '11':
                print("Exiting the program")
                break

            #call appropriate method based on that choice
            if choice == '1':
                self.addAccount(bank)
            elif choice == '2':
                self.removeAccount(bank)
            elif choice == '3':
                self.findAccount(bank)
            elif choice == '4':
                self.deposit(bank)
            elif choice == '5':
                self.withdraw(bank)
            elif choice == '6':
                self.showBalance(bank)
            elif choice == '7':
                self.addMonthlyInterest(bank)
            elif choice == '8':
                self.listAllAccounts(bank)
            elif choice == '9':
                self.closeAccount(bank)
            elif choice == '10':
                self.displayAccountDetails(bank)
            else:
                print("Invalid choice, please enter a number between 1 and 11.")


    def promptForAccountNumberAndPIN(self, bank):
        while True:
                account_number_input = input("Enter account number: ")

                #check if the account number is numeric using isNumeric method
                if not BankUtility.isNumeric(account_number_input):
                    print("Invalid input. Please enter a valid numeric account number.")
                    continue #ask for input again if its not numeric

                #convert account number to integer after validation
                account_number = int(account_number_input)

                #try to find the account by account number
                account = bank.findAccount(account_number)
                if account is None:
                    print(f"Account not found for account number: {account_number}")
                    return None

                #ask for pin
                pin = input("Enter PIN: ")

                #validate pin
                if account.isValidPIN(pin):
                    return account
                else:
                    print("Invalid PIN")
                    return None

    def addAccount(self, bank):
        # Code to add a new account
        # Ask for account details
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")

        #loop until a valid SSN is entered
        while True:
            ssn = input("Enter SSN (e.g., 999-99-9999 (without dashes)): ")
            try:
                new_account = Account(firstname, lastname, ssn)
                break #break out of loop if ssn is valid
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid SSN (9 digits")

        if bank.addaccounttobank(new_account):
            print(f"Account for {firstname} {lastname} added successfully.")
        else:
            print("No more accounts available.")

        self.listAllAccounts(bank)

    def removeAccount(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            bank.removeAccountFromBank(account)
            print(f"Account {account.account_number} has been removed.")
            self.listAllAccounts(bank)

    def findAccount(self, bank):
        while True:
            account_number_input = input("Enter account number to find: ")

            # Check if the input is numeric using isNumeric method
            if not BankUtility.isNumeric(account_number_input):
                print("Invalid input. Please enter a valid numeric account number.")
                continue  # Ask for input again if it's not numeric

            # Convert account number to integer after validation
            account_number = int(account_number_input)

            # Try to find the account by account number
            account = bank.findAccount(account_number)
            if account:
                print(f"Account found: {account.to_string()}")
                break
            else:
                print(f"Account not found for account number: {account_number}")
                break


    def deposit(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            amount = int(input("Enter deposit amount (in dollars, e.g., 5 for $5: ")) * 100 #convert dollars to cents
            account.deposit(amount)
            print(
                f"Deposited {amount / 100:.2f} to account {account.account_number}. New balance: {account.balance / 100:.2f}")

    def withdraw(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            #ensure the input is an integer (cents)
            while True:
                try:
                    amount = int(input("Enter withdrawl amount (in dollars, e.g., 5 for $5): ")) * 100 #convert dollars to cents
                    if amount <= 0:
                        raise ValueError("Withdrawal amount must be greater than 0.")
                    new_balance = account.withdraw(amount) #perform withdrawal in cents
                    print(f"New balance after withdrawl: ${new_balance / 100:.2f}")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid withdrawal amount.")

    def showBalance(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            print(f"Account balance: ${account.balance / 100:.2f}")

    def addMonthlyInterest(self, bank):
        try:
            interest_rate = float(input("Enter annual interest rate (e.g., 2.5 for 2.5%): "))
            bank.addMonthlyInterest(interest_rate)
            print(f"Monthly interest added at {interest_rate}% annual rate.")
        except ValueError as e:
            print(f"Error: {e}")


    def listAllAccounts(self, bank):
        bank.listAllAccounts()

    def closeAccount(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            bank.removeAccountFromBank(account)
            print(f"Account {account.account_number} has been closed.")

    def displayAccountDetails(self, bank):
        account = self.promptForAccountNumberAndPIN(bank)
        if account is not None:
            print(f"Account Details: {account.to_string()}")

manager = BankManager()
manager.main()