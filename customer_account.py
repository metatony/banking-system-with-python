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
    
    def get_interest_rate(self):
        return self.interest_rate
    
    def get_overdraft_limit(self):
        return self.overdraft_limit
    
    def get_account_type(self):
        return self.account_type
    
    # Method to get the account number
    def get_account_no(self):
        return self.account_no
    
    # method to calculate interest rate for savings accounts
    def calculate_interest(self):

        if self.get_interest_rate() > 0:
            interest = self.get_balance() * (self.get_interest_rate() / 100)
            return interest
        else:
            return 0
        
    
    # Method to display the account menu and get user choice
    def account_menu(self):
        while True:
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
            try:
                option = int(input("Choose your option: "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
            
        return option
    
    # Method to print details of the customer
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.get_first_name()) 
        print("Last name: %s" %self.get_last_name()) 
        print("Account No: %s" %self.get_account_no()) 
        print("Address: %s" %self.get_address()[0]) 
        print(" %s" %self.get_address()[1]) 
        print(" %s" %self.get_address()[2]) 
        print(" %s" %self.get_address()[3]) 
        print(" ")
   
    # Method to run various account options based on user input
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                try:
                    amount = float(input("\n Please enter amount to be deposited: ")) 
                    self.deposit(amount)
                    self.print_balance()
                except ValueError:
                    print("\nInvalid input. Please enter a valid numeric value for the amount.")
                
            elif choice == 2:
                #ToDo (withdrawal logic)
                try:
                    amount = float(input("\n Please enter amount to be withdrawn: "))
                    self.withdraw(amount)
                    self.print_balance()
                except ValueError:
                    print("\nInvalid input. Please enter a valid numeric value for the amount.")
                
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
                
            elif choice == 4:
                #STEP A.4.2
                fname = input("\n Enter new customer first name: ").capitalize() 
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ").capitalize()
                self.update_last_name(sname)
                print('Customer name has been updated successfully')


            elif choice == 5:
                #ToDo (update customer address)
                                
                house_no = input("\nPlease enter your house number: ")
                street = input("\nPlease enter your street name: ").capitalize()
                city = input("\nPlease enter your city name: ").capitalize()
                post_code = input("\nPlease enter your post code: ").capitalize()
                
                self.update_address(house_no, street, city, post_code)
                      
            elif choice == 6:
                self.print_details()
                
            elif choice == 7:
                # self.calculate_interest()
                if self.get_interest_rate() >= 0:
                    if self.get_interest_rate() > 0:
                        interest = self.get_balance() * (self.get_interest_rate() / 100)
                        print(f"\nInterest of {interest:.2f} calculated for the account.")
                        return interest
                else:
                    print("\nYou are a Current account user. you don't have interest rate")
                
                
            elif choice == 8:
                if self.get_overdraft_limit() <= 0:
                    print('You\'re not eligible for an overdraft')
                else:
                    print("\nYour overdraft limit is 1000")
                
            elif choice == 9:
                loop = 0
        print ("\n Exit account operations")
        
        
        
    def serialize(self):
        return {
            "fname": self.get_first_name(),
            "lname": self.get_last_name(),
            "address": self.get_address(),
            "account_no": self.get_account_no(),
            "balance": self.get_balance(),
            "account_type": self.get_account_type(),
            "interest_rate": self.get_interest_rate(),
            "overdraft_limit": self.get_overdraft_limit()
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