
# this is the super class
class Person:
    # Constructor to initialize the object with provided attributes
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address
    
    # Method to update the first name
    def update_first_name(self, fname):
        self.fname = fname
    
    # Method to update the last name
    def update_last_name(self, lname):
        self.lname = lname
                
    # Method to get the first name
    def get_first_name(self):
        return self.fname
    
    # Method to get the last name
    def get_last_name(self):
        return self.lname
        
    # Method to update the address
    def update_address(self, addr):
        self.address = addr
        print("Address updated successfully!")
    
    # Method to get the address
    def get_address(self):
        return self.address