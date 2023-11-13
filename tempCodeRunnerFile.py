import tkinter as tk

user_data = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "Thato": "thato123"
}



class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")

        # Initial content 

        #App name
        self.label = tk.Label(root, text="Our Application Name")
        self.label.pack(pady=10)


        #Login Credentials
        self.username = tk.Label(root, text="Username")
        self.usernameInput = tk.Entry(root)

        self.password = tk.Label(root, text="Password")
        self.passwordInput = tk.Entry(root, text="Enter Password")

    

        self.username.pack()
        self.usernameInput.pack()
        self.password.pack()
        self.passwordInput.pack()

        # Button to login
        self.login = tk.Button(root, text="Login", command=self.loginSuccess)
        self.login.pack(pady=10)

    #This function is to change the interface

    
    def loginSuccess(self):

        passwordText = self.passwordInput.get()

        if passwordText == user_data["user1"]:
            
            print("It's the same")

            # This is what changes the interface // allow access
            self.label.config(text="Content changed! Button was clicked.")
            self.root.configure(bg="#F5EEC8")
            self.deposit = tk.Button(root, text="Transfer Funds", command=self.transferFunds)
            self.deposit.pack()
        else:
            print("Password is incorrect")
            self.label.configure(text="Password is incorrect")


    def transferFunds(self):
        self.transferButton = tk.Button(root, text="How much to deposit")
        self.transferButton.pack()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.configure(bg="#555843")
    app = MyApp(root)
    root.mainloop()