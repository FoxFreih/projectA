import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd
import time
import Funcfile
from pandas import DataFrame


# reading single line from csv file
def readcsv(num):
    # openning file out of the function
    cols = pd.read_csv("IssueLocation.csv")
    return cols.iloc[num]


def fillcombobox():
    import pandas as pd
    xl = pd.read_csv("IssueTime.csv")
    lst = []
    for i in range(1, len(xl['product'])):
        if not (xl['product'][i] in lst):
            lst.append(xl['product'][i])
    return lst




x = 10
y = 10
class IssueRequest:

    def __init__(self):
        global lst1
        self.app = tk.Tk()
        self.app.geometry('320x250')
        self.app.title("customer")

        self.name=tk.StringVar()
        self.product=tk.StringVar()
        self.issue=tk.StringVar()
        self.place=tk.StringVar()

        tk.Label(self.app,text = "customer name:").grid(column=0,row=0,padx=x,pady=y)
        tk.Entry(self.app,textvariable=self.name).grid(column=1,row=0,padx=x,pady=y)



        tk.Label(self.app,text = "product name:").grid(column=0, row=1,padx=x,pady=y)
        lst=fillcombobox()
        self.compo1=ttk.Combobox(self.app,textvariable=self.product,values=lst)
        self.compo1.current(0)
        self.compo1.bind("<<ComboboxSelected>>", self.callback)
        self.compo1.grid(column=1,row=1,padx=x,pady=y)


        tk.Label(self.app,text = "place:").grid(column=0, row=3,padx=x,pady=y)
        tk.Entry(self.app,textvariable=self.place).grid(column=1,row=3,padx=x,pady=y)
        tk.Button(self.app,text="send",width=15,command=self.click).grid(column=0,row=4,padx=x+5,pady=y+5)
        self.app.mainloop()

    def callback(self,events):
        import pandas as pd
        xl = pd.read_csv("IssueTime.csv")
        lst1 = []
        for i in range(len(xl['discription'])):
            if self.compo1.get() == xl['product'][i]:
                lst1.append(xl['discription'][i])
        tk.Label(self.app, text="issue:").grid(column=0, row=2, padx=x, pady=y)
        global compo2
        compo2 = ttk.Combobox(self.app, textvariable=self.issue, values=lst1)
        compo2.update()
        compo2.current(0)
        compo2.grid(column=1, row=2, padx=x, pady=y)

    def click(self):
        customerIssue = {"name": self.name.get(),
                         "product": self.product.get(),
                         "issue": self.issue.get(),
                         "place": self.place.get(),
                         "time": time.asctime(),
                         "taken": 0}
        df = pd.DataFrame([customerIssue])
        df.to_csv('customerissue.csv', mode='a', index=False, header=0)

        self.app.destroy()
        #Funcfile.AdminScreen()
print("hi")
if __name__=='__main__':
    #print("name : hi")
    IssueRequest()
#issue.__init__()


