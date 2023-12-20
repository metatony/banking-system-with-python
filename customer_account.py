# Importing the Person class from the Person module
from Person import Person


# defining this CustomerAccount class as a subclass inheriting from Person
class CustomerAccount(Person):
    # Constructor to initialize the object with provided attributes
    def __init__(self, fname, lname, address, account_no, balance, account_type, interest_rate, overdraft_limit):
        # Calling the constructor of the parent class (Person)
        Person.__init__(self, fname, lname, address)
        self.account_no = account_no
        self.balance = float(balance)
        self.interest_rate = interest_rate
        self.overdraft_limit = overdraft_limit
        self.account_type = account_type
        
    
    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance+=amount
    
    # Method to withdraw money out of the account
    def withdraw(self, amount):
        #ToDo
        # self.balance -= amount
        
        # method to calculate overdraft limit
        if self.get_balance() - amount >= -self.overdraft_limit:
            # super().withdraw(amount)
            self.balance -= amount
        else:
            print("\nTransaction failed. Overdraft limit exceeded.")

    
    # Method to print the current account balance
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
    
    # Method to get the current account balance
    def get_balance(self):
        return self.balance
    
    # Method to get the account number
    def get_account_no(self):
        return self.account_no
    
    # method to calculate interest rate for savings accounts
    def calculate_interest(self):
        # interest = self.get_balance() * (self.interest_rate / 100)
        # # self.deposit(interest)
        # print(f"\nInterest of {interest:.2f} added to the account.")
        
        if self.interest_rate > 0:
            interest = self.get_balance() * (self.interest_rate / 100)
            print(f"\nInterest of {interest:.2f} calculated for the account.")
            return interest
        else:
            print("\nYou are a Current account user. You don't have an interest rate.")
            return 0
        
        
    

    # Method to display the account menu and get user choice
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Calculate interest")
        print ("8) Overdraft limit")
        print ("9) Back")
        print (" ")
        # Getting user input for menu choice
        option = int(input ("Choose your option: "))
        return option
    
    # Method to print details of the customer
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname) 
        print("Last name: %s" %self.lname) 
        print("Account No: %s" %self.account_no) 
        print("Address: %s" %self.address[0]) 
        print(" %s" %self.address[1]) 
        print(" %s" %self.address[2]) 
        print(" %s" %self.address[3]) 
        print(" ")
   
    # Method to run various account options based on user input
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                amount = float(input("\n Please enter amount to be deposited: ")) 
                self.deposit(amount)
                self.print_balance()
                
            elif choice == 2:
                #ToDo (withdrawal logic)
                amount = float(input("\n Please enter amount to be withdrawn: "))
                self.withdraw(amount)
                self.print_balance()
                
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
                
            elif choice == 4:
                #STEP A.4.2
                fname = input("\n Enter new customer first name: ") 
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ") 
                self.update_last_name(sname)
                print('Customer name has been updated successfully')


            elif choice == 5:
                #ToDo (update customer address)
                addr = input("\n Enter new customer address: ")
                self.update_address(addr)
                print("\n Customer address updated successfully!")
                #pass
                
            elif choice == 6:
                self.print_details()
                
            elif choice == 7:
                # self.calculate_interest()
                if self.interest_rate >= 0:
                    self.calculate_interest()
                else:
                    print("\nYou are a Current account user. you don't have interest rate")
                
                
            elif choice == 8:
                if self.overdraft_limit <= 0:
                    print('You\'re not eligible for an overdraft')
                else:
                    print("\nYour overdraft limit is 1000")
                
            elif choice == 9:
                loop = 0
        print ("\n Exit account operations")
        
        
    def serialize(self):
        return {
            "fname": self.fname,
            "lname": self.lname,
            "address": self.address,
            "account_no": self.account_no,
            "balance": self.balance,
            "account_type": self.account_type,
            "interest_rate": self.interest_rate,
            "overdraft_limit": self.overdraft_limit
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            data["fname"],
            data["lname"],
            data["address"],
            data["account_no"],
            data["balance"],
            data["account_type"],
            data["interest_rate"],
            data["overdraft_limit"]
        )