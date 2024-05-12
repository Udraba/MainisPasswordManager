import random
import string
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("670x800")
        self.root.title("Maini's Cool Password Adventure")
        self.root.iconbitmap("Maini.ico")

        self.mainframe = tk.Frame(self.root, background="dark khaki")
        self.mainframe.pack(fill="both", expand=True)

        self.text = ttk.Label(self.mainframe, text="Maini's Cool Password Adventure", background="dark khaki", font=("Impact", 30), foreground="black")
        self.text.grid(row=0, column=0)

        self.text_login = ttk.Label(self.mainframe, text="Where do you want to login", background="dark khaki", font=("Impact", 15), foreground="black")
        self.text_login.grid(row=1, column=0)

        self.field_login = ttk.Entry(self.mainframe)
        self.field_login.grid(row=2, column=0, sticky="NWES")


        self.text_user = ttk.Label(self.mainframe, text="Username or Email", font=("Impact", 15), background="dark khaki", foreground="black")
        self.text_user.grid(row=3, column=0)


        self.set_user_field = ttk.Entry(self.mainframe)
        self.set_user_field.grid(row=4,column=0, pady=10, sticky="NWES")


        self.text_password_options = ttk.Label(self.mainframe, text="Password Options", font=("Impact", 25), background="dark khaki", foreground="black")
        self.text_password_options.grid(row=5, column=0)

        self.text_password = ttk.Label(self.mainframe, text="Password", font=("Impact", 15), background="dark khaki", foreground="black")
        self.text_password.grid(row=6, column=0)

        self.set_password_field = ttk.Entry(self.mainframe)
        self.set_password_field.grid(row=7,column=0, pady=10, sticky="NWES")

        self.text_or = ttk.Label(self.mainframe, text="Or", font=("Impact", 20), background="dark khaki", foreground="black")
        self.text_or.grid(row=8, column=0)


        self.text_generate = ttk.Label(self.mainframe, text="Generate a password", font=("Impact", 15), background="dark khaki", foreground="black")
        self.text_generate.grid(row=9, column=0)

        self.text_length = ttk.Label(self.mainframe,  text="Enter the Length of your password (Leave empty if you don't want to generate a password)", font=("Impact", 10), background="dark khaki", foreground="black")
        self.text_length.grid(row=10,column=0)

        self.field_length = ttk.Entry(self.mainframe)
        self.field_length.grid(row=11, column=0, sticky="NWES")

        self.confirm_button = ttk.Button(self.mainframe, text="Confirm Data and save to file", command=self.writfilestation)
        self.confirm_button.grid(row=12, column=0)
        
        self.image_of_maini = Image.open("Maini.png")
        self.image_of_maini = ImageTk.PhotoImage(self.image_of_maini)

        self.image_label = ttk.Label(self.mainframe, image=self.image_of_maini, background="dark khaki")
        self.image_label.grid(row=14, column=0)

        
        self.root.mainloop()

    def writfilestation(self):
        #Normal Password
        NormalPassword = self.set_password_field.get()
        #Platform to login to
        platform = self.field_login.get()
        #Username/email
        Username = self.set_user_field.get()

        password = ""
        #Password Generator
        characters = string.ascii_letters
        characters += string.punctuation
        characters += string.digits

        #Checking if there is input in the Type the length of the password field
        if self.field_length.get() == "":
            password = NormalPassword
            length = 0
        else:
             length = int(self.field_length.get())

        RandomPassword = ""
        
        if length >= 1:
            for i in range(length):
                RandomPassword += random.choice(characters)
                password = RandomPassword
        elif NormalPassword == "":
            password = "no password given"
        else:
            password = NormalPassword
        
        text2 = " Username/Email: "+Username
        text3 = " Password: "+password
        file = open("passwords.txt", "a")
        file.write("\n")
        file.write("\n"+platform+":")
        file.write("\n"+text2)
        file.write("\n"+text3)
        file.close

    
if __name__ == "__main__":
    App()