import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import time
import Login
import customer


def cal_travel_time(x1, y1, x2, y2):
    import math
    speed = 30000
    a = x2 - x1
    b = y2 - y1
    distance = math.sqrt(a * a + b * b)
    time = distance / speed
    return time

def Shibuts():
    messagebox.showinfo(title="ok", message="shibuts is ok")
    print("Hello")

def addProduct():
    pass





def load_admin_screen():
    pass


class AdminScreen(Login.Page):

    def __init__(self, app, root, *args, **kwargs):
        Login.Page.__init__(self, app, root, *args, **kwargs)
        self.height = 250
        self.width = 600
        self.title = "Admin"
        self.configure(bg='white')
        shibuts = Button(self, text="Shibuts", font=('Times New Roman', 14), bg='red', fg='white', padx=10,
                         command=Shibuts)
        shibuts.place(relx=0.5, rely=0.75, anchor=CENTER)
        AddIssue = Button(self, text="AddIssueRequest", font=('Times New Roman', 14), bg='dark green', fg='white',
                          padx=10,
                          command=self.addIssueRequest)
        AddIssue.place(relx=0.53, rely=0.45, anchor=CENTER)
        AddFault = Button(self, text="AddFault", font=('Times New Roman', 14), bg='blue4', fg='white', padx=10,
                          command=self.addFault)
        AddFault.place(relx=0.25, rely=0.45, anchor=CENTER)
        AddProduct = Button(self, text="AddProduct", font=('Times New Roman', 14), bg='goldenrod', fg='white',
                            padx=10,
                            command=addProduct)
        AddProduct.place(relx=0.8, rely=0.45, anchor=CENTER)


    def click(self):
        pass

    def addIssueRequest(self):
        cus=customer.IssueRequest(self.app,self.root,self)
        cus.start()
        cus.show()

    def addFault(self):
        fault  = FaultScreen(self.app,self.root,self)
        print(type(self))
        print(type(self.root))
        print(type(self.app))
        fault.start()
        fault.show()


class FaultScreen(Login.Page):
    def __init__(self, app, root, parent, *args, **kwargs):
        x = 10
        y = 10
        Login.Page.__init__(self, app, root, *args, **kwargs)
        self.height = 250
        self.width = 350
        self.title = "AddFault"
        self.parent = parent
        self.product = tk.StringVar()
        self.discription = tk.StringVar()
        self.time = tk.StringVar()
        self.IssueLevel = tk.StringVar()

        tk.Label(self, text="product:").grid(column=0, row=0, padx=x, pady=y)
        tk.Entry(self, textvariable=self.product).grid(column=1, row=0, padx=x, pady=y)
        tk.Label(self, text="discription:").grid(column=0, row=1, padx=x, pady=y)
        tk.Entry(self, textvariable=self.discription).grid(column=1, row=1, padx=x, pady=y)
        tk.Label(self, text="time:").grid(column=0, row=3, padx=x, pady=y)
        tk.Entry(self, textvariable=self.time).grid(column=1, row=3, padx=x, pady=y)
        tk.Label(self, text="IssueLevel:").grid(column=0, row=4, padx=x, pady=y)
        lst = ['*', '**']
        compo1 = ttk.Combobox(self, textvariable=self.IssueLevel, values=lst)
        compo1.current(0)
        compo1.grid(column=1, row=4, padx=x, pady=y)
        tk.Button(self, text="send", width=15, command=self.click).grid(column=0, row=5, padx=x + 5, pady=y + 5)


    def click(self):
        Faultwrite = {"product": self.product.get(),
                         "discription": self.discription.get(),
                         "time": self.time.get(),
                         "IssueLevel":self.IssueLevel.get()}
        df = pd.DataFrame([Faultwrite])
        df.to_csv('IssueTime.csv', mode='a', index=False,header=0)
        self.destroy()
        self.parent.show()


def load_tech_screen():
    root1 = Tk()
    root1.geometry("500x500")
    root1.title("tech")
    root1.mainloop()



