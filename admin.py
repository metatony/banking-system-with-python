from Person import Person

# defining this Admin class as a subclass inheriting from Person
class Admin(Person):
    # Constructor to initialize the object with provided attributes
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        Person.__init__(self, fname, lname, address)
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
        
    
    # Method to set the user name
    def set_username(self, uname):
        self.user_name = uname
     
    # Method to get the user name
    def get_username(self):
        return self.user_name
    
    # Method to get the address
    def get_address(self):
        return self.address      
    
    # method to update the password
    def update_password(self, password):
        self.password = password
    
    # method to get the password
    def get_password(self):
        return self.password
    
    # method to set the full admin rights
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right
        
    # Method to check if the admin has full admin rights
    def has_full_admin_right(self):
        return self.full_admin_rights
    
    
    def update_own_info(self):
        while True:
            print(" ")
            print("Update Admin Information:")
            print(" ")
            print("1) Update Admin name")
            print("2) Update address")
            print("3) Print Admin info")
            print("4) Back")
            
            try:
                option = int(input("Choose an option: "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid integer.")                        
            
        
        if option == 1:
            fname = input("\n Enter new admin first name: ").capitalize()
            self.update_first_name(fname)
            sname = input("\n Enter new admin last name: ").capitalize()
            self.update_last_name(sname)
            print('Admin name has been updated successfully')

        elif option == 2:
            new_address = input("\n Enter new address: ")
            self.update_address(new_address)
            print("\n Address updated successfully!")
        elif option == 3:
            print("\n Admin information")
            self.print_admin_details()
        elif option == 4:
            print("\n Going back to admin menu.")
        else:
            print("\n Invalid option. Please try again.")
            
        return option

            
    # Method to print details of the admins
    def print_admin_details(self):
        print("First name: %s" %self.get_first_name()) 
        print("Last name: %s" %self.get_last_name()) 
        print("Address: %s" %self.get_address()[0]) 
        print(" %s" %self.get_address()[1]) 
        print(" %s" %self.get_address()[2]) 
        print(" %s" %self.get_address()[3]) 
        print(" ")


    def serialize(self):
        return {
            "fname": self.get_first_name(),
            "lname": self.get_last_name(),
            "address": self.get_address(),
            "user_name": self.get_username(),
            "password": self.get_password(),
            "full_admin_rights": self.has_full_admin_right()
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            data["fname"],
            data["lname"],
            data["address"],
            data["user_name"],
            data["password"],
            data["full_admin_rights"]
        )

