from customer_account import CustomerAccount
from admin import Admin
import json

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data_from_file()
    
    def load_bank_data(self):
        
        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, "Savings", 3.5, 0)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, "Current", 0, 1000)
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, "Savings", 3.5, 0)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, "Current", 0, 1000)
        self.accounts_list.append(customer_4)
        
        
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        #STEP A.2
        found_admin = None
        for a in self.admins_list:
            user_name = a.get_username()
            if user_name == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        #STEP A.3
        found_customers = []
        for customer in self.accounts_list:
            if customer.get_last_name() == customer_lname:
                found_customers.append(customer)

        if not found_customers:
            print("\n No customer with last name %s found! Try again...\n" % customer_lname)

        return found_customers

    def main_menu(self):
        #print the options you have
        while True: # added exception handling to prevent system from crashing
            print()
            print()
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("Welcome to the Python Bank System")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Admin login")
            print ("2) Quit Python Bank System")
            print (" ")
            try:
                option = int(input("Choose your option: "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
            
        return option


    def run_main_options(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        
        self.save_bank_data_to_file()
        print ("\n Thank-You for stopping by the bank!")

    # method to transfer money to another user
    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        #ToDo
        sender = None
        receiver = None

        # Find the sender
        for customer in self.accounts_list:
            if customer.get_last_name() == sender_lname:
                sender = customer
                break

        # Find the receiver
        for customer in self.accounts_list:
            if customer.get_last_name() == receiver_lname and customer.get_account_no() == int(receiver_account_no):
                receiver = customer
                break

        if sender is None:
            print(f"\nSender with last name {sender_lname} not found!")
            return

        if receiver is None:
            print(f"\nReceiver with last name {receiver_lname} and account number {receiver_account_no} not found!")
            return

        # Check if the sender has enough balance
        if sender.get_balance() >= amount:
            # Deduct the amount from the sender
            sender.withdraw(amount)
            # Add the amount to the receiver
            receiver.deposit(amount)

            print("\nTransaction successful!")
        else:
            print("\nInsufficient funds in the sender's account. Transaction failed.")

                
    # method to allow admins to login to the system
    def admin_login(self, username, password):
		  #STEP A.1
        found_admin = self.search_admins_by_name(username)
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
            
            else: # added an else statement to prevent system from crashing or progressing when a wrong password is input
                msg = "\n Incorrect password"
                found_admin = None
        return msg, found_admin

    def admin_menu(self, admin_obj):
        #print the options you have
        while True:
            print (" ")
            print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("1) Transfer money")
            print ("2) Customer account operations & profile settings")
            print ("3) Delete customer")
            print ("4) Print all customers detail")
            print ("5) Update admin information")
            print ("6) Print all admins detail")
            print ("7) Generate management report")
            print ("8) Sign out")
            print (" ")
            
            try:
                option = int(input("Choose your option: "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")
                
        return option
     
    # Method to delete customer
    def delete_customer(self, customer_obj):
        if customer_obj in self.accounts_list:
            self.accounts_list.remove(customer_obj)
            print("\nCustomer deleted successfully!")
        else:
            print("\nCustomer not found!")


    def run_admin_options(self, admin_obj):                               
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                try:
                    sender_lname = input("\n Please input sender surname: ").capitalize()
                    amount = float(input("\n Please input the amount to be transferred: "))
                    receiver_lname = input("\n Please input receiver surname: ").capitalize()
                    receiver_account_no = input("\n Please input receiver account number: ")
                    self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)
                except ValueError:
                    print("\nInvalid input. Please enter a valid numeric value for the amount.")

                                    
            elif choice == 2:
                #STEP A.4
                customer_name = input("\n Please input customer surname :\n").capitalize() # added the capitalize object to prevent case sensitive error
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    customer_account[0].run_account_options() 
            
            elif choice == 3:
                #Todo (logic to delete customer)
                try:
                    customer_name = input("\n Please input customer surname to delete:\n").capitalize()
                    customer_account = self.search_customers_by_name(customer_name)
                    if customer_account:
                        self.delete_customer(customer_account[0])
                        self.save_bank_data_to_file()

                    else:
                        print("\nNo customer found with the provided surname. Deletion aborted.")
                except ValueError:
                    print("\nInvalid input. Please enter a valid customer surname.")

                
            elif choice == 4:
                #Todo (print all customers details)
                self.print_all_accounts_details()
                
            elif choice == 5:  # Option to update admin's own information
                admin_obj.update_own_info()
                self.save_bank_data_to_file()
                
            elif choice == 6:  # Option to update admin's own information
                self.print_all_admin_details()
                
            elif choice == 7:  # option to generate reports
                self.generate_management_report()
            
            elif choice == 8:
                loop = 0
                self.save_bank_data_to_file()
        print ("\n Exit account operations")

    #method to print all customer account details
    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")
                
    def print_all_admin_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.admins_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_admin_details()
                print("------------------------")
                
    # method to read and write to a file
    def save_bank_data_to_file(self, filename="bank_data.txt"):

        with open(filename, 'w') as file:
        # Serialize and write each customer and admin to the file
            for customer in self.accounts_list:
                file.write(json.dumps(customer.serialize()) + '\n')
            for admin in self.admins_list:
                file.write(json.dumps(admin.serialize()) + '\n')


    def load_bank_data_from_file(self, filename="bank_data.txt"):
        try:
            with open(filename, "r") as file:
                # Read each line and deserialize the object
                for line in file:
                    data = json.loads(line)
                    if "account_type" in data:
                        # Deserialize and append to accounts_list
                        account = CustomerAccount.deserialize(data)
                        self.accounts_list.append(account)
                    elif "user_name" in data:
                        # Deserialize and append to admins_list
                        admin = Admin.deserialize(data)
                        self.admins_list.append(admin)

                print("Data loaded successfully.")

        except FileNotFoundError:
            print("File not found. No data loaded.")
        except json.JSONDecodeError:
            print("Error decoding JSON. No data loaded.")
            
    # method to generate reports
    def generate_management_report(self):
        total_customers = len(self.accounts_list)
        total_money = sum(customer.get_balance() for customer in self.accounts_list)
        total_interest = sum(customer.calculate_interest() for customer in self.accounts_list if hasattr(customer, 'calculate_interest'))
        total_overdrafts = sum(customer.overdraft_limit for customer in self.accounts_list if hasattr(customer, 'overdraft_limit'))

        # Print the management report
        print("\nManagement Report:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print(f"a) Total number of customers in the system: {total_customers}")
        print(f"b) Sum of all money the customers currently have in their bank account: {total_money:.2f}")
        print(f"c) Sum of interest rate payable to all accounts for one year: {total_interest:.2f}")
        print(f"d) Total amount of overdrafts currently taken by all customers: {total_overdrafts:.2f}")




app = BankSystem()
app.run_main_options()



