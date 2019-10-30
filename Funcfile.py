import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import time
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


class AdminScreen(object):

    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x250")
        self.root.title("Admin")
        self.root.configure(bg='white')
        shibuts = Button(self.root, text="Shibuts", font=('Times New Roman', 14), bg='red', fg='white', padx=10,
                         command=Shibuts)
        shibuts.place(relx=0.5, rely=0.75, anchor=CENTER)
        AddIssue = Button(self.root, text="AddIssueRequest", font=('Times New Roman', 14), bg='dark green', fg='white',
                          padx=10,
                          command=self.addIssueRequest)
        AddIssue.place(relx=0.5, rely=0.45, anchor=CENTER)
        AddFault = Button(self.root, text="AddFault", font=('Times New Roman', 14), bg='blue4', fg='white', padx=10,
                          command=self.addFault)
        AddFault.place(relx=0.25, rely=0.45, anchor=CENTER)
        AddProduct = Button(self.root, text="AddProduct", font=('Times New Roman', 14), bg='goldenrod', fg='white',
                            padx=10,
                            command=addProduct)
        AddProduct.place(relx=0.76, rely=0.45, anchor=CENTER)

    def mainloop(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()

    def click(self):
        pass

    def addIssueRequest(self):
        self.root.destroy()
        customer.IssueRequest()


    def addFault(self):
        self.root.destroy()
        #app.mainloop()
        fault  = FaultScreen()


class FaultScreen:
    def __init__(self):
        self.app = tk.Tk()
        x = 10
        y = 10
        self.app.geometry('320x250')
        self.app.title("AddFault")
        self.product = tk.StringVar()
        self.discription = tk.StringVar()
        self.time = tk.StringVar()
        self.IssueLevel = tk.StringVar()

        tk.Label(self.app, text="product:").grid(column=0, row=0, padx=x, pady=y)
        tk.Entry(self.app, textvariable=self.product).grid(column=1, row=0, padx=x, pady=y)
        tk.Label(self.app, text="discription:").grid(column=0, row=1, padx=x, pady=y)
        tk.Entry(self.app, textvariable=self.discription).grid(column=1, row=1, padx=x, pady=y)
        tk.Label(self.app, text="time:").grid(column=0, row=3, padx=x, pady=y)
        tk.Entry(self.app, textvariable=self.time).grid(column=1, row=3, padx=x, pady=y)
        tk.Label(self.app, text="IssueLevel:").grid(column=0, row=4, padx=x, pady=y)
        lst = ['*', '**']
        compo1 = ttk.Combobox(self.app, textvariable=self.IssueLevel, values=lst)
        compo1.current(0)
        compo1.grid(column=1, row=4, padx=x, pady=y)
        tk.Button(self.app, text="send", width=15, command=self.click).grid(column=0, row=5, padx=x + 5, pady=y + 5)

        #self.app.mainloop()

    def click(self):
        Faultwrite = {"product": self.product.get(),
                         "discription": self.discription.get(),
                         "time": self.time.get(),
                         "IssueLevel":self.IssueLevel.get()}
        df = pd.DataFrame([Faultwrite])
        df.to_csv('IssueTime.csv', mode='a', index=False,header=0)
        self.app.destroy()
        AdminScreen()
    



def load_tech_screen():
    root1 = Tk()
    root1.geometry("500x500")
    root1.title("tech")
    root1.mainloop()



