# import design
#
#
# class TechnicianScreen(design.Page):
#
#     def __init__(self, app, root, *args, **kwargs):
#         design.Page.__init__(self, app, root, *args, **kwargs)
#         self.height = 250
#         self.width = 600
#         self.title = "Technician"
#         self.configure(bg='white')
#
# import tkinter as tk
#
# class ExampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         t = SimpleTable(self, 10,2)
#         t.pack(side="top", fill="x")
#         t.set(0,0,"Hello, world")
#
# class SimpleTable(tk.Frame):
#     def __init__(self, parent, rows=10, columns=2):
#         # use black background so it "peeks through" to
#         # form grid lines
#         tk.Frame.__init__(self, parent, background="black")
#         self._widgets = []
#         for row in range(rows):
#             current_row = []
#             for column in range(columns):
#                 label = tk.Label(self, text="%s/%s" % (row, column),
#                                  borderwidth=0, width=10)
#                 label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
#                 current_row.append(label)
#             self._widgets.append(current_row)
#
#         for column in range(columns):
#             self.grid_columnconfigure(column, weight=1)
#
#
#     def set(self, row, column, value):
#         widget = self._widgets[row][column]
#         widget.configure(text=value)
#
# if __name__ == "__main__":
#     app = ExampleApp()
#     app.mainloop()
from tkinter import *
from tksheet import Sheet
import pandas as pd
import design
import tkinter as tk
from tkinter import ttk


class TechnicianScreen(design.Page):
    def __init__(self, app, root, *args, **kwargs):
        design.Page.__init__(self, app, root, * args, **kwargs)
        self.height = 600
        self.width = 1050
        self.status = []
        self.title = "Technician schedule"
        self.grid_columnconfigure(0, weight =1)
        self.grid_rowconfigure(0, weight =1)
        #self.configure(bg="white")
        self.cols = pd.read_csv("shibuts.csv")
        self.Cols=self.cols[["product","issue","location","time","critical/notCritical"]]
        self.row_count = len(self.cols)
        #print(self.row_count)
        self.data = [self.Cols.iloc[i] for i in range(self.row_count)]
        labelTop = tk.Label(self,
                            text="Issue status",font=('Times New Roman', 14))
        labelTop.grid(column=0, row=0)
        labelTop.place(relx=0.830, rely=0.075)
        for i in range(self.row_count):
            self.var = tk.StringVar()
            if self.cols.iloc[i,5]=="**":

                self.comboExample = ttk.Combobox(self,textvariable=self.var,
                                    values=[
                                        "treated",
                                        "not treated",
                                        "becomes normal"])
            if self.cols.iloc[i, 5] == "*":
                self.comboExample = ttk.Combobox(self, textvariable=self.var,
                                                 values=[
                                                     "treated",
                                                     "not treated"])

            self.status.append(self.var)
            self.comboExample.grid(column=0, row=i+1)
            self.comboExample.place(relx=0.830, rely=0.120+(i*0.04), relheight=0.04
                              , relwidth=0.140)
            self.comboExample.current(1)
        self.sdem = Sheet(self,
                          align = "w",
                          header_align = "center",
                          row_index_align = "center",
                          show = True,
                          column_width = 140,
                          row_index_width = 50,
                          data_reference = self.data,
                          headers=["Product","IssueDescription","Location","Time","**Critical/*Normal"],
                          )
        self.sdem.enable_bindings(("single",
                                   "drag_select",
                                   "column_drag_and_drop",
                                   "row_drag_and_drop",
                                   "column_select",
                                   "row_select",
                                   "column_width_resize",
                                   "double_click_column_resize",
                                   "row_width_resize",
                                   "column_height_resize",
                                   "arrowkeys",
                                   "row_height_resize",
                                   "double_click_row_resize"))
        self.sdem.edit_bindings(True)
        self.sdem.grid(row = 0, column = 0,sticky="nswe")
        self.sdem.place(relx=0.05, rely=0.067, relheight=0.751
                            , relwidth=0.780)
        self.sdem.highlight_cells(row = 0, column = 0, bg = "orange", fg = "blue")
        self.sdem.highlight_cells(row = 0, bg = "orange", fg = "blue", canvas = "row_index")
        self.sdem.highlight_cells(column = 0, bg = "orange", fg = "blue", canvas = "header")
        self.send= Button(self, text="send", font=('Times New Roman', 15), bg='orange', fg='blue', padx=5,
                       command=self.save).place(relx=0.880, rely=0.85)
    def save(self):
        for i in range(self.row_count):
            if self.status[i].get() == "treated":
                self.cols.drop(i,inplace=True)
            if self.status[i].get() == "becomes normal":
                self.cols.iat[i,5]="*"
        self.cols.to_csv('shibuts.csv', mode='w', index=False, header=["id","product","issue","location","time","critical/notCritical"])

