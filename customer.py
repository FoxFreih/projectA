import time
import tkinter as tk
from tkinter import ttk
import pandas as pd
import design
def genID():
    cols = pd.read_csv("customerissues.csv")
    id= cols.iloc[-1]
  #  print(id)
    return str(int(16)+1)
# reading single line from csv file
def readcsv(num):
    # openning file out of the function
    cols = pd.read_csv("IssueLocation.csv")
    return cols.iloc[num]


def fillcombobox():
    xl = pd.read_csv("product.csv")
    lst = []
    for i in range(len(xl)):
        if not (xl['productName'][i] in lst):
            lst.append(xl['productName'][i])
    return lst


x = 10
y = 10

#print(type(LOGIN.Page))
class IssueRequest(design.Page):


    def __init__(self, app, root, parent, *args, **kwargs):
        design.Page.__init__(self, app, root, *args, **kwargs)
        self.height = 250
        self.width = 350
        self.title = "Customer"
        self.parent = parent
        global lst1
        self.name = tk.StringVar()
        self.product = tk.StringVar()
        self.issue = tk.StringVar()
        self.my_place = tk.StringVar()

        tk.Label(self, text="customer name:").grid(column=0, row=0, padx=x, pady=y)
        tk.Entry(self, textvariable=self.name).grid(column=1, row=0, padx=x, pady=y)

        tk.Label(self, text="product name:").grid(column=0, row=1, padx=x, pady=y)
        lst = fillcombobox()
        self.compo1 = ttk.Combobox(self, textvariable=self.product, values=lst)
        self.compo1.current(0)
        self.compo1.bind("<<ComboboxSelected>>", self.callback)
        self.compo1.grid(column=1, row=1, padx=x, pady=y)

        tk.Label(self, text="place:").grid(column=0, row=3, padx=x, pady=y)
        tk.Entry(self, textvariable=self.my_place).grid(column=1, row=3, padx=x, pady=y)
        tk.Button(self, text="send", width=15, command=self.click).grid(column=0, row=4, padx=x + 5, pady=y + 5)

    def callback(self, events):
        import pandas as pd
        xl = pd.read_csv("IssueTime.csv")
        lst1 = []
        for i in range(len(xl['discription'])):
            if self.compo1.get() == xl['product'][i]:
                lst1.append(xl['discription'][i])
        tk.Label(self, text="issue:").grid(column=0, row=2, padx=x, pady=y)
        global compo2
        compo2 = ttk.Combobox(self, textvariable=self.issue, values=lst1)
        compo2.update()
        compo2.current(0)
        compo2.grid(column=1, row=2, padx=x, pady=y)

    def click(self):
        from Funcfile import  addresTocoordinates
        customerIssue = {"name": self.name.get(),
                         "product": self.product.get(),
                         "issue": self.issue.get(),
                         "place": self.my_place.get(),
                         "time": time.asctime(),
                         "taken": 0,
                         "coordinate": addresTocoordinates(self.my_place.get()),
                         "ciID":genID()}
        df = pd.DataFrame([customerIssue])
        df.to_csv('customerissue.csv', mode='a', index=False, header=0)

        self.destroy()
        if self.parent is not None:
            self.parent.show()
        else:
            self.root.destroy()


class App(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        login = IssueRequest(self, root, None)
        login.place(x=0, y=0, relwidth=1, relheight=1)
        login.show()

    def add_page(self, page):
        print(type(page))
        page.place(x=0, y=0, relwidth=1, relheight=1)

    def show(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
