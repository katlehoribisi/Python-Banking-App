import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import PhotoImage

user_data = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "Thato": "thato123"
}

# ---- ---- ---- ---- ---- --- --- #

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seascape Bank")

        #Bank money
        self.currentBalance = 0
        self.savingsBalance = 0
        self.debitBalance = 0
        self.totalBalance = 0
        self.savedUpMoney = 0
        # Initial content 

        #App name
        self.loginText = tk.Label(root, text="Sescape Bank", font=("Arial",20), bg="#555843", fg="#D0D4CA")
        self.loginText.pack(pady=10)


        #Login Credentials
        self.email = tk.Label(root, text="Email", font=("Arial",14), bg="#555843", fg="white")
        self.emailInput = tk.Entry(root)

        self.password = tk.Label(root, text="Password", font=("Arial",14), bg="#555843", fg="white")
        self.passwordInput = tk.Entry(root, text="Enter Password", show="*")

        self.email.pack(pady=4)
        self.emailInput.pack(padx=10)
        self.password.pack(pady=4)
        self.passwordInput.pack(pady=10)


        self.accessButtons = tk.Frame(root)
        self.accessButtons.pack(anchor="center")
        # Button to login
        self.login = tk.Button(self.accessButtons, text="Login", command=self.loginSuccess, font=("Arial",14), bg="#D0D4CA", fg="#3A4D39")
        self.login.pack(side=tk.RIGHT)
        
        #Button to Register
        self.register = tk.Button(self.accessButtons, text="Register", command=self.registerUser, font=("Arial",14), bg="#D0D4CA", fg="#3A4D39")
        self.register.pack(side=tk.RIGHT)


    #This function is to change the interface

# ---- ---- ---- ---- ---- --- --- #
    def registerUser(self):
        #Remove every previous element
        self.password.pack_forget()
        self.passwordInput.pack_forget()
        self.email.pack_forget()
        self.emailInput.pack_forget()
        self.login.pack_forget()
        self.register.pack_forget()
        self.accessButtons.pack_forget()
        self.loginText.pack_forget()
        
        #Create Register Frame
        self.registerFrame = tk.Frame(root, bg="#555843")
        self.registerFrame.pack(pady=20)

        #Asking user credentials
        self.name = tk.Label(self.registerFrame, text="Name: ", font=("Arial",14), bg="#555843", fg="white")
        self.nameEntry = tk.Entry(self.registerFrame)
        self.surname = tk.Label(self.registerFrame, text="Surname: ", font=("Arial",14), bg="#555843", fg="white")
        self.surnameEntry = tk.Entry(self.registerFrame)
        self.email = tk.Label(self.registerFrame, text="Email: ", font=("Arial",14), bg="#555843", fg="white")
        self.emailEntry = tk.Entry(self.registerFrame)
        self.password = tk.Label(self.registerFrame, text="Password: ", font=("Arial",14), bg="#555843", fg="white")
        self.passwordEntry = tk.Entry(self.registerFrame, show="*")


        #Packing User Credentials
        self.name.pack(anchor="w")
        self.nameEntry.pack()
        
        self.surname.pack(anchor="w")
        self.surnameEntry.pack()
        
        self.email.pack(anchor="w")
        self.emailEntry.pack()
        
        self.password.pack(anchor="w")
        self.passwordEntry.pack()

        #Final Register button
        self.registerButton = tk.Button(self.registerFrame, text="Register" ,command=self.registerSuccess, font=("Arial",14), bg="#D0D4CA", fg="#3A4D39")
        self.registerButton.pack(pady=20)

# ---- ---- ---- ---- ---- --- --- #

    def registerSuccess(self):

        user_data[self.emailEntry.get()] = self.passwordEntry.get()
        

        self.registerFrame.pack_forget()

        #App name
        self.loginText = tk.Label(root, text="Sescape Bank", font=("Arial",20), bg="#555843", fg="#D0D4CA")
        self.loginText.pack(pady=10)


        #Login Credentials
        self.email = tk.Label(root, text="Email", font=("Arial",14), bg="#555843", fg="white")
        self.emailInput = tk.Entry(root)

        self.password = tk.Label(root, text="Password", font=("Arial",14), bg="#555843", fg="white")
        self.passwordInput = tk.Entry(root, text="Enter Password", show="*")

        self.email.pack(pady=4)
        self.emailInput.pack(padx=10)
        self.password.pack(pady=4)
        self.passwordInput.pack(pady=10)


        self.accessButtons = tk.Frame(root)
        self.accessButtons.pack(anchor="center")
        # Button to login
        self.login = tk.Button(self.accessButtons, text="Login", command=self.loginSuccess, font=("Arial",14), bg="#D0D4CA", fg="#3A4D39")
        self.login.pack(side=tk.RIGHT)
        #Button to Register
        self.register = tk.Button(self.accessButtons, text="Register", command=self.registerUser, font=("Arial",14), bg="#D0D4CA", fg="#3A4D39")
        self.register.pack(side=tk.RIGHT)

# ---- ---- ---- ---- ---- --- --- #
# ---- ---- ---- ---- ---- --- --- #
    # This is what changes the interface // allow access
    def loginSuccess(self):
        
        emailText = self.emailInput.get()
        passwordText = self.passwordInput.get()
        if emailText in user_data and passwordText == user_data[emailText]:

            # Hide the elements that are from old login interface
            self.loginText.pack_forget()
            self.register.pack_forget()
            self.accessButtons.pack_forget()
            
            self.mainSectionFrame = tk.Frame(root, bg="#D0D4CA")
            self.mainSectionFrame.pack(pady=30)


            self.mainButtons = tk.Frame(self.mainSectionFrame, bg="#D0D4CA")
            self.mainButtons.pack(anchor="center")

            self.welcome = tk.Label(self.mainButtons, font=("Helvetica",30), text="Welcome to Seascape Bank", bg="#D0D4CA", fg="#6A9C89")
            self.welcome.pack(anchor="n", pady=25)
            self.deposit = tk.Button(self.mainButtons, text="Transfer Funds", command=self.transferFunds, bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1")
            self.deposit.pack(side=tk.RIGHT)
            self.goods = tk.Button(self.mainButtons, text="Purchase Goods", command=self.purchaseGoods, bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1")
            self.goods.pack(side = tk.LEFT)

            #Banner
            self.banner = tk.PhotoImage(file='newBanner.png')
            self.seascapeBanner = tk.Label(self.mainSectionFrame, image=self.banner)
            self.seascapeBanner.pack(pady=80)

            # Hide the elements that are from old login interface
            self.password.pack_forget()
            self.passwordInput.pack_forget()
            self.email.pack_forget()
            self.emailInput.pack_forget()
            self.login.pack_forget()

            #Page Styling
            self.root.configure(bg="#D0D4CA")
        else:
            messagebox.showerror("Error","Something is wrong with your user or password")

# ---- ---- ---- ---- ---- --- --- #
    def purchaseGoods(self):
        #Remove Main Section Interface
        self.mainSectionFrame.pack_forget()

        #Go back to main screen
        def backPurchase():
            self.mainSectionFrame.pack(pady=30)
            self.purchaseGoods.pack_forget()
            self.backPurchaseFrame.pack_forget()
            self.root.configure(bg="#D0D4CA")

        #Back Button creation and positioning
        self.backPurchaseFrame = tk.Frame(root)
        self.backPurchaseFrame.pack(side = "top", anchor = "nw", pady=10, padx=10)
        backPurchase = tk.Button(self.backPurchaseFrame, text="Go back", command = backPurchase, bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1")
        backPurchase.pack()

        #Purchase Goods Frame
        self.purchaseGoods = tk.Frame(root, bg="#F5EEC8")
        self.purchaseGoods.pack()

        #Purchase R10 airtime
        def purchaseTenAirtime():
            #Subtract from user balance amount
            if self.debitBalance >= 10:
                newBalance = self.debitBalance - 10
                self.debitBalance = newBalance
                self.success = tk.Label(self.purchaseGoods, text="Purchase Success", font=("Arial",14), bg="#FFDBAA", fg="#A2C579")            
                self.success.pack()
            else:
                self.notsuccess = tk.Label(self.purchaseGoods, text="Insufficient Funds", font=("Arial",14), bg="#860A35", fg="white")            
                self.notsuccess.pack()  
                

        #Show on interface The Buy button and it's label
        tenAirtime = tk.Label(self.purchaseGoods, text="Purchase R10 Airtime", font=("Arial",14), bg="#F5EEC8", fg="#3A4D39")
        tenAirtimeBuy = tk.Button(self.purchaseGoods, text="Buy", command=purchaseTenAirtime, font=("Arial",14), bg="#FFB7B7", fg="#FFFFDD")
        tenAirtime.pack()
        tenAirtimeBuy.pack()

        #Purchase R1000 electricity
        def purchase_electricity():
            #Subtract from user balance amount
            if self.debitBalance >= 1000:
                newBalance = self.debitBalance - 1000
                self.debitBalance = newBalance
                self.success = tk.Label(self.purchaseGoods, text="Purchase Success", font=("Arial",14), bg="#FFDBAA", fg="#A2C579")            
                self.success.pack()
            else:
                self.notsuccess = tk.Label(self.purchaseGoods, text="Insufficient Funds", font=("Arial",14), bg="#860A35", fg="white")            
                self.notsuccess.pack()   

        #Show on interface The Buy button and it's label
        fiftyElec = tk.Label(self.purchaseGoods, text="Purchase R1000 Electricity", font=("Arial",14), bg="#F5EEC8", fg="#3A4D39")
        purc_elec = tk.Button(self.purchaseGoods, text="Buy", command=purchase_electricity, font=("Arial",14), bg="#FFB7B7", fg="#FFFFDD")
        fiftyElec.pack()
        purc_elec.pack()

        #Page Styling
        self.root.configure(bg="#F5EEC8")
# ---- ---- ---- ---- ---- --- --- #

    def transferFunds(self):
        #Remove Main Section Interface
        self.mainSectionFrame.pack_forget()

        #back Button to go back to main interface
        def backTransfer():
            self.transferFundsFrame.pack_forget()
            self.mainSectionFrame.pack(pady=30)
            self.backFrame.pack_forget()
            self.accountsFrame.pack_forget()
            self.root.configure(bg="#D0D4CA")

        #Current Balance Config
        self.balance_var = StringVar()
        self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")

        def addMoney():
            if not hasattr(self, 'deposit_frame_visible') or not self.deposit_frame_visible:
                self.depositFrame.pack(anchor="center")
                self.deposit_frame_visible = True
            else:
                self.depositFrame.pack_forget()
                self.deposit_frame_visible = False


        def confirmDeposit():
            depositMoney = int(self.depositEntry.get())
            self.debitBalance += depositMoney
            self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")
            self.debitVar.set(f"Debit Account: R{self.debitBalance}")
            self.depositEntry.delete(0, tk.END)

            self.depositFrame.pack_forget()

        def transferDebit():
            #This updates the values live on the interface
            if self.debitBalance <= 0:
                messagebox.showerror("Error","There is nothing in your debit balance.")
            else:
                self.savingsVar.set(f"Savings Account: R{self.savingsBalance}")
                self.debitVar.set(f"Debit Account: R{self.debitBalance}")
                self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")

                #Display deposit amount entry when "transfer" clicked.
                if not hasattr(self, 'deposit_entry_visible') or not self.deposit_entry_visible:
                    self.debitAmountFrame.pack(side=tk.RIGHT)
                    self.deposit_entry_visible = True
                else:
                    self.debitAmountFrame.pack_forget()
                    self.deposit_entry_visible = False

        def transferSavings():
            #This updates the values live on the interface
            if self.savingsBalance <= 0:
                messagebox.showerror("Error","There is nothing in your savings.")
            else:
                self.savingsVar.set(f"Savings Account: R{self.savingsBalance}")
                self.debitVar.set(f"Debit Account: R{self.debitBalance}")
                self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")

                #Display deposit amount entry when "transfer" clicked.
                if not hasattr(self, 'savings_entry_visible') or not self.savings_entry_visible:
                    self.savingAmountFrame.pack(side=tk.RIGHT)
                    self.savings_entry_visible = True
                else:
                    self.savingAmountFrame.pack_forget()
                    self.savings_entry_visible = False

        def confirmToSavings():
            #Transfer all money from debit to savings.
            debitAmount = self.debitAmount.get()
            if int(debitAmount) > self.debitBalance:
                messagebox.showerror("Error","There's not enough funds to transfer.")
            else:
                self.savingsBalance += int(debitAmount)
                newDebit = self.debitBalance - int(debitAmount)
                self.debitBalance = newDebit
            
            #This updates the values live on the interface
            self.savingsVar.set(f"Savings Account: R{self.savingsBalance}")
            self.debitVar.set(f"Debit Account: R{self.debitBalance}")
            self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")
            
            self.debitAmount.delete(0, tk.END)
            self.debitAmountFrame.pack_forget()

        def confirmToDebit():
            #Transfer all money from debit to savings.
            savedSavings = self.savingsAmount.get()
            if int(savedSavings) > self.savingsBalance:
                messagebox.showerror("Error","There's not enough funds to transfer.")
            else:
                self.debitBalance += int(savedSavings)
                newSavings = self.savingsBalance - int(savedSavings)
                self.savingsBalance = newSavings
            
            #This updates the values live on the interface
            self.savingsVar.set(f"Savings Account: R{self.savingsBalance}")
            self.debitVar.set(f"Debit Account: R{self.debitBalance}")
            self.balance_var.set(f"Current Balance: R{self.debitBalance + self.savingsBalance}")
            
            self.savingsAmount.delete(0, tk.END)
            self.savingAmountFrame.pack_forget()   

        def on_enter_key(event):
            confirmDeposit()
        def on_enter_key_debit(event):
            confirmToDebit()
        def on_enter_key_savings(event):
            confirmToSavings()

        #Back Button creation and positioning
        self.backFrame = tk.Frame(root)
        self.backFrame.pack(side = "top", anchor = "nw", pady=10, padx=10)
        backTransfer = tk.Button(self.backFrame, text="Go back", command = backTransfer, bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1")
        backTransfer.pack()

        #Transfer Funds Frame
        self.transferFundsFrame = tk.Frame(root, bg="#A7D397")
        self.transferFundsFrame.pack()
        
        self.balance = tk.Label(self.transferFundsFrame, textvariable=self.balance_var, font=("Arial",14), bg="#A7D397", fg="#236f3e")

        #Deposit Frame
        self.depositFrame = tk.Frame(self.transferFundsFrame, bg="#A7D397")
        self.depositEntry = tk.Entry(self.depositFrame)
        self.depositButton = tk.Button(self.depositFrame, text="Confirm", font=("Helvetica",10), command=confirmDeposit, bg="#a7c9c9",fg="#4c6973")

        # Bind the Enter key press event to the confirm_deposit function
        self.depositEntry.bind("<Return>", on_enter_key)

        self.transferLabel = tk.Label(self.depositFrame, text="Deposit Amount: ", font=("Arial",14), bg="#A7D397", fg="#395e48")
        self.transferLabel.pack()
        self.depositEntry.pack(side=tk.LEFT)
        self.depositButton.pack(side=tk.RIGHT, padx=5)

        #This is a button to deposit money
        self.addMoney = tk.Button(self.transferFundsFrame, text="Deposit Money", bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1", command=addMoney)
        self.addMoney.pack()


        #Account Text Variables
        self.savingsVar = StringVar()
        self.savingsVar.set(f"Savings Account: R{self.savingsBalance}")
        self.debitVar = StringVar()
        self.debitVar.set(f"Debit Account: R{self.debitBalance}")
        
        #Accounts Frame
        self.accountsFrame = tk.Frame(root, bg="#A7D397", height=250, width=450)
        self.accountsFrame.pack(pady=140, side=tk.LEFT,anchor="nw")

        #Savings Frame
        self.savingsFrame = tk.Frame(self.accountsFrame, bg="#A7D397", height=50, width=350)
        self.savingsFrame.pack(pady=30, padx=20, anchor="w")

        self.savingsText = tk.Label(self.savingsFrame, textvariable=self.savingsVar, font=("Arial",14), bg="#A7D397", fg="#236f3e", width=25)
        self.savingsText.pack(side=tk.LEFT, anchor="w")

        #Debit Frame
        self.debitFrame = tk.Frame(self.accountsFrame, bg="#A7D397", height=50, width=350)
        self.debitFrame.pack(pady=30, padx=20, anchor="w")

        self.debitText = tk.Label(self.debitFrame, textvariable=self.debitVar, font=("Arial",14), bg="#A7D397", fg="#236f3e", width=25 )
        self.debitText.pack(side=tk.LEFT)
        

        # Transfer Button for savings
        self.transferSavings = tk.Button(self.savingsFrame, text="Transfer", command=transferSavings, font=("Arial",10), bg="#6A9C89", fg="white")
        self.transferSavings.pack(side=tk.LEFT, padx=5, pady=5, anchor="w")

        # Frame for the amount to transfer savings entry
        self.savingAmountFrame = tk.Frame(self.savingsFrame, bg="#caddbe")
        self.savingsAmount = tk.Entry(self.savingAmountFrame, bd=0, bg="#caddbe")
        self.savingsAmount.pack(side=tk.LEFT)

        # Ok button for savings
        self.savingsAmountConfirm = tk.Button(self.savingAmountFrame, text="Ok", command=confirmToDebit,bg="#d0e1c5",fg="#506146")
        self.savingsAmountConfirm.pack(side=tk.LEFT)

        # Bind the Enter key press event to the confirmToDebit function
        self.savingsAmount.bind("<Return>", on_enter_key_debit)

        # Transfer Button for debit
        self.transferDebit = tk.Button(self.debitFrame, text="Transfer", command=transferDebit, font=("Arial",10), bg="#6A9C89", fg="white")
        self.transferDebit.pack(side=tk.LEFT, padx=5, pady=5, anchor="w")

        # Frame for the amount to transfer debit entry
        self.debitAmountFrame = tk.Frame(self.debitFrame, bg="#caddbe")
        self.debitAmount = tk.Entry(self.debitAmountFrame, bd=0, bg="#caddbe")
        self.debitAmount.pack(side=tk.LEFT)

        # Ok button for debit
        self.debitAmountConfirm = tk.Button(self.debitAmountFrame, text="Ok", command=confirmToSavings, bg="#d0e1c5",fg="#506146"   )
        self.debitAmountConfirm.pack(side=tk.LEFT)

        # Bind the Enter key press event to the confirmToSavings function
        self.debitAmount.bind("<Return>", on_enter_key_savings)


        self.balance.pack()


        #Page Styling
        self.root.configure(bg="#A7D397")
# ---- ---- ---- ---- ---- --- --- #

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.configure(bg="#555843")
    app = MyApp(root)
    root.mainloop()

