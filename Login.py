from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import Funcfile
import time
from technician import printf
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import messagebox, ttk


# form design
# Funcfile.cal_travel_time(31.3238353,35.0711483,31.3856301,34.7637722)
class Page(tk.Frame):
    def __init__(self, app, root, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.app = app
        self.root = root
        self.height = None
        self.width = None
        self.title = None

    def show(self):
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.root.title(self.title)
        self.lift()

    def start(self):
        self.app.add_page(self)


class LogIn(Page):
    def __init__(self, app, root, *args, **kwargs):
        Page.__init__(self, app, root, * args, **kwargs)
        self.height = 650
        self.width = 500
        self.title = "System Login"
        self.username = StringVar()
        self.userpassword = StringVar()
        self.configure(bg='white')
        t = Label(self, text="Login Form", font=('Times New Roman', 30), bd=20, fg='green', bg='white', height=1)
        t.pack()
        form = Frame(self)
        form.pack(side=LEFT)
        form.configure(bg='white')
        name1 = Label(form, text="Username:", font=('Times New Roman', 20), bg='white', bd=30).grid(row=1, sticky=W)
        password1 = Label(form, text="password:", font=('Times New Roman', 20), bg='white', bd=30).grid(row=2, sticky=W)
        name2 = Entry(form, textvariable=self.username).grid(row=1, column=2)
        password2 = Entry(form, textvariable=self.userpassword, show=("*")).grid(row=2, column=2)
        login = Button(self, text="Login", font=('Times New Roman', 14), bg='green', fg='white', padx=10,
                       command=self.checkUser)
        place = login.place(relx=0.5, rely=0.75, anchor=CENTER)
        ############ changing the image show #########
        # canvas = Canvas(self,width=208, height=204)#,bg='white')
        # canvas.place(relx=0.5, rely=0.3, anchor=CENTER)
        # img = PhotoImage(file="images.png")
        # canvas.create_image(10, 5, image=img, anchor=NW)
        ########another way of showing the image #########
        # self.pack(fill=BOTH, expand=1)
        load = Image.open("images.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(relx=0.5, rely=0.3, anchor=CENTER)

    # reading and checking username and password from excel file
    def connection(self, name, password):
        df = pd.read_excel('UsersList.xlsx', 'users')
        for i in df.index:
            if df['UserName'][i] == name:
                if str(df['password'][i]) == password:
                    return True
                else:
                    return False
        return False

    # checking the user details , printing a message according to the function result
    def checkUser(self):
        username = self.username.get()
        userpassword = self.userpassword.get()
        if username == "*":
            if userpassword == "":
                screen = Funcfile.AdminScreen(self.app,self.root)
                screen.start()
                screen.show()


            else:
                messagebox.showinfo(title="hello admin", message="Login failed: Invalid password")
        else:
            # call connection function to verify if the user & the password saved in the system database
            data = self.connection(username, userpassword)
            # print(data)
            if data == True:
                Funcfile.load_tech_screen()
            else:
                messagebox.showinfo(title="hello user", message="Login failed: Invalid username or password")


# main class for building frame
class App(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self,root, *args, **kwargs)

        login = LogIn(self,root)
        login.place(x=0, y=0, relwidth=1, relheight=1)
        login.show()

    def add_page(self,page):
        page.place(x=0, y=0, relwidth=1, relheight=1)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
