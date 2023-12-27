from customer_account import CustomerAccount

class SavingsAccount(CustomerAccount):
    def __init__(self, fname, lname, address, account_no, balance, interest_rate):
        CustomerAccount.__init__(self, fname, lname, address, account_no, balance)
        # self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * (self.get_interest_rate() / 100)
        self.deposit(interest)
        print(f"\nInterest of {interest:.2f} added to the account.")

    def account_menu(self):
        # Override the account_menu method to include savings-specific options
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Calculate interest")
        print("8) Back")
        print(" ")
        # Getting user input for menu choice
        option = int(input("Choose your option: "))
        return option
    
    
class CurrentAccount(CustomerAccount):
    def __init__(self, fname, lname, address, account_no, balance, overdraft_limit):
        CustomerAccount.__init__(self, fname, lname, address, account_no, balance)
        # self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.get_overdraft_limit:
            super().withdraw(amount)
        else:
            print("\nTransaction failed. Overdraft limit exceeded.")

    def account_menu(self):
        # Override the account_menu method to include current account-specific options
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Calculate interest")
        print("8) Back")
        print(" ")
        # Getting user input for menu choice
        option = int(input("Choose your option: "))
        return option
