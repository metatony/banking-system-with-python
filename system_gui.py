from bank_system import BankSystem
import tkinter as tk
    

# Admin login gui class
class AdminLogin:
    
    def __init__(self):
    
        self.mw = tk.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.title("Admin Login")
        
        self.mw.geometry("400x400")
        self.admin_username_label = tk.Label(self.mw, text = "Enter Admin Username")
        self.admin_username_entry = tk.Entry(self.mw, width = 20)
        
        self.admin_username_label.pack(side="top")
        self.admin_username_entry.pack(side="top")
        
        
        self.admin_password_label = tk.Label(self.mw, text = "Enter Admin Password")
        self.admin_password_entry = tk.Entry(self.mw, width = 20)
        
        self.admin_password_label.pack(side="top")
        self.admin_password_entry.pack(side="top")
        
        self.login_button = tk.Button(self.mw, text ="Login", command =lambda: self.login(self.admin_username_entry.get(), self.admin_password_entry.get()))
        self.login_button.pack(side = "top")
        
        
        tk.mainloop()
        
# function to login the admin   
    def login(self, username, password):
        msg, admin_obj = bank_system_obj.admin_login(username, password)
        if admin_obj != None:
            self.mw.destroy()
            AdminOptions(admin_obj)
        else:
            tk.messagebox.showerror("Error", msg)


# admin option GUI class
class AdminOptions:
    def __init__(self, admin_obj):
        self.mw = tk.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("400x400")
        self.mw.title("Admin Options")
        
        self.admin_obj = admin_obj
        
        welcome_text = "Welcome Admin: %s %s" %(admin_obj.get_first_name(), admin_obj.get_last_name())
        welcome_label = tk.Label(self.mw, text = welcome_text)
        welcome_label.pack()
        
        
        self.transfer_button = tk.Button(self.mw, text ="Transfer Money", command =lambda: self.makeTransfer()).pack()
        
        self.customer_account_ops_button = tk.Button(self.mw, text ="Customer account operations & profie settings", command =lambda: self.customerAccountOptions()).pack()
        
        self.delete_customer_button = tk.Button(self.mw, text ="Delete Customer").pack() ######
        
        self.print_all_customer_button = tk.Button(self.mw, text ="Print all customers detail").pack() #####
        
        self.update_admin_details_button = tk.Button(self.mw, text ="Update Admin Information", command =lambda: self.updateAdminDetails()).pack() #####
        
        self.print_all_admin_details_button = tk.Button(self.mw, text ="Print all Admin Information").pack() #######
    
        self.mgmt_report_button = tk.Button(self.mw, text ="Generate Management Report").pack() #######
        
        self.sign_out_button = tk.Button(self.mw, text ="Sign Out", command =lambda: self.sign_out()).pack()
        
        
# function to initiate transfer
    def makeTransfer(self):
        TransferMoney()

# function to display customer account options screen
    def customerAccountOptions(self):
        CustomerAccountOptions()

# function to update admin details
    def updateAdminDetails(self):
        AdminDetails(self.admin_obj)
    
# function to sign out the admin
    def sign_out(self):
        self.mw.destroy()
        AdminLogin()

# class for transfer money GUI 
class TransferMoney:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("400x400")
        
        self.sender_label = tk.Label(self.mw, text = "Enter Sender Surname:").pack()
        self.sender_entry = tk.Entry(self.mw, width=20)
        self.sender_entry.pack()
        
        self.amount_label = tk.Label(self.mw, text = "Enter Amount to be transferred:").pack()
        self.amount_entry = tk.Entry(self.mw, width=20)
        self.amount_entry.pack()
        
        self.receiver_label = tk.Label(self.mw, text = "Enter Receiver Surname:").pack()
        self.receiver_entry = tk.Entry(self.mw, width=20)
        self.receiver_entry.pack()
        
        self.receiver_account_label = tk.Label(self.mw, text = "Enter Receiver Account:").pack()
        self.receiver_account_entry = tk.Entry(self.mw, width=20)
        self.receiver_account_entry.pack()
        
        
        self.transfer_btn = tk.Button(self.mw, text ="Do Transfer", command =lambda: self.transfer_money(self.sender_entry.get(), self.receiver_entry.get(), 
                                                                                                              self.receiver_account_entry.get(), self.amount_entry.get())).pack()
        
    def transfer_money(self, sender_lname, receiver_lname, receiver_account_no, amount):
        msg, transfer_success = bank_system_obj.transferMoney(sender_lname, receiver_lname, receiver_account_no, float(amount))
        if transfer_success:
            tk.messagebox.showinfo("Success", msg)
            self.mw.destroy()
        else:
            tk.messagebox.showerror("Error", msg)


# class for customer account options GUI 
class CustomerAccountOptions:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("800x400")
        
        self.surname_label = tk.Label(self.mw, text = "Enter Customer Surname:")
        self.surname_label.grid(row = 0, column=0)
        
        self.surname_entry = tk.Entry(self.mw, width=20)
        self.surname_entry.grid(row = 0, column=1)
        self.surname_entry.bind("<KeyPress>", self.on_entry_focus)
        
        self.search_btn = tk.Button(self.mw, text ="Search", command =lambda: self.search(self.surname_entry.get()))
        self.search_btn.grid(row = 0, column=2)
        
        self.deposit_btn = tk.Button(self.mw, text ="Deposit Money")
        self.withdraw_btn = tk.Button(self.mw, text ="Withdraw Money")
        self.balance_btn = tk.Button(self.mw, text ="Check Balance")
        self.check_details_btn = tk.Button(self.mw, text = "Check/Update Customer Details")
        
    
    def on_entry_focus(self, event):
        self.clearButtonsFromGrid()
        
    def search(self, customer_lname):
        self.customer_account = bank_system_obj.search_customers_by_name(customer_lname)
        if self.customer_account != None:
            self.deposit_btn.grid(row = 1, column=0, columnspan=3)
            self.withdraw_btn.grid(row = 2, column=0, columnspan=3)
            self.balance_btn.grid(row = 3, column=0, columnspan=3)
            self.check_details_btn.grid(row = 4, column = 0, columnspan=3)
            
        else:
            self.clearButtonsFromGrid()
            tk.messagebox.showerror("Error", "Customer not found")
            
    
    def clearButtonsFromGrid(self):
        self.deposit_btn.grid_forget()
        self.withdraw_btn.grid_forget()
        self.balance_btn.grid_forget()
        self.check_details_btn.grid_forget()

   
# class for admin details GUI 
class AdminDetails:
    def __init__(self, admin_obj):
        self.mw = tk.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("800x400")
        self.mw.title("Admin Details "+admin_obj.get_first_name() + " " + admin_obj.get_last_name())
        
        
        tk.Label(self.mw, text = "Firstname:").grid(row=3, column=1)
        self.fname_entry = tk.Entry(self.mw, width=20)
        self.fname_entry.insert(0, admin_obj.get_first_name())
        self.fname_entry.grid(row=3, column=2)
        
        tk.Label(self.mw, text = "Lastname:").grid(row=4, column=1)
        self.lname_entry = tk.Entry(self.mw, width=20)
        self.lname_entry.insert(0, admin_obj.get_last_name())
        self.lname_entry.grid(row=4, column=2)
        
        tk.Label(self.mw, text = "Address:").grid(row=5, column=1)
        
        address = admin_obj.get_address()
        
        tk.Label(self.mw, text = "House No:").grid(row=6, column=1)
        
        self.house_no_entry = tk.Entry(self.mw, width=20)
        self.house_no_entry.insert(0, address[0])
        self.house_no_entry.grid(row=6, column=2)
        
        tk.Label(self.mw, text = "Street:").grid(row=7, column=1)
        self.street_entry = tk.Entry(self.mw, width=20)
        self.street_entry.insert(0, address[1])
        self.street_entry.grid(row=7, column=2)
        
        
        tk.Label(self.mw, text = "City:").grid(row=8, column=1)
        self.city_entry = tk.Entry(self.mw, width=20)
        self.city_entry.insert(0, address[2])
        self.city_entry.grid(row=8, column=2)
        
        tk.Label(self.mw, text = "Postcode:").grid(row=9, column=1)
        self.postcode_entry = tk.Entry(self.mw, width=20)
        self.postcode_entry.insert(0, address[3])
        self.postcode_entry.grid(row=9, column=2)
        
        
        self.update_btn = tk.Button(self.mw, text ="Update Details", command =lambda: 
                                         self.update_own_info(admin_obj, self.fname_entry.get(), self.lname_entry.get(),
                                                                  [self.house_no_entry.get(), self.street_entry.get(), self.city_entry.get(),
                                                                   self.postcode_entry.get()]))
        self.update_btn.grid(row=10, column=2)
        
         
        
bank_system_obj = BankSystem()
AdminLogin()
