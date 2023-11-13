import tkinter as tk
from tkinter import messagebox

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
        self.currentBalance = 500
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
        self.name.pack()
        self.nameEntry.pack()
        
        self.surname.pack()
        self.surnameEntry.pack()
        
        self.email.pack()
        self.emailEntry.pack()
        
        self.password.pack()
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
            buy = 10
            newBalance = self.currentBalance - buy
          

            if newBalance > 10:
                self.currentBalance = newBalance
                self.currentBalance - buy
                self.success = tk.Label(self.purchaseGoods, text="Purchase Success", font=("Arial",14), bg="#FFDBAA", fg="#A2C579")            
                self.success.pack()
            else:
                self.success = tk.Label(self.purchaseGoods, text="Insufficient Funds", font=("Arial",14), bg="#860A35", fg="white")            
                self.success.pack()  
                

        #Show on interface The Buy button and it's label
        tenAirtime = tk.Label(self.purchaseGoods, text="Purchase R10 Airtime", font=("Arial",14), bg="#F5EEC8", fg="#3A4D39")
        tenAirtimeBuy = tk.Button(self.purchaseGoods, text="Buy", command=purchaseTenAirtime, font=("Arial",14), bg="#FFB7B7", fg="#FFFFDD")
        tenAirtime.pack()
        tenAirtimeBuy.pack()

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
            self.root.configure(bg="#D0D4CA")

        #Back Button creation and positioning
        self.backFrame = tk.Frame(root)
        self.backFrame.pack(side = "top", anchor = "nw", pady=10, padx=10)
        backTransfer = tk.Button(self.backFrame, text="Go back", command = backTransfer, bg="#6A9C89", font=("Helvetica",15), fg="#d0e5d1")
        backTransfer.pack()

        #Transfer Funds Frame
        self.transferFundsFrame = tk.Frame(root, bg="#A7D397")
        self.transferFundsFrame.pack()
        
        self.transferLabel = tk.Label(self.transferFundsFrame, text="How much to deposit", font=("Arial",14), bg="#A7D397", fg="#236f3e")
        self.balance = tk.Label(self.transferFundsFrame, text=f"Current Balance: R{self.currentBalance}", font=("Arial",14), bg="#A7D397", fg="#236f3e")
        
        self.transferLabel.pack()
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


