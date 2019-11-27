from tkinter import *
from tksheet import Sheet
import pandas as pd
import design
import tkinter as tk
from tkinter import ttk


class TechnicianScreen(design.Page):
    def __init__(self, app, root,id, *args, **kwargs):
        design.Page.__init__(self, app, root, * args, **kwargs)
        self.height = 600
        self.width = 1050
        self.id=id
        self.status = []
        self.title = "Technician schedule"
        self.grid_columnconfigure(0, weight =1)
        self.grid_rowconfigure(0, weight =1)
        #self.configure(bg="white")
        self.cols = pd.read_csv("techissue.csv")
        self.cols=self.cols.loc[self.cols.ID == self.id, :]
        self.Cols=self.cols[["ID","customerName","product","issue","location","crit","issueID"]]
        self.row_count = len(self.cols)
        #print(self.row_coun t)
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
                          headers=["ID","customerName","product","issue","location","crit","issueID"],
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
        self.dff=pd.read_csv("customerissue.csv")

        count1 = len(self.dff)
        for i in range(self.row_count):
            if self.status[i].get() == "treated":
                for j in range(count1):
                    if self.dff.iloc[j]["ID"]== self.cols.iloc[i]["issueID"]:
                        self.dff.iat[j, 5] = "2"
            if self.status[i].get() == "not treated":
                for j in range(count1):
                    if self.dff.iloc[j]["ID"] == self.cols.iloc[i]["issueID"]:
                        self.dff.iat[j, 5] = "0"
        self.dff.to_csv('customerissue.csv', mode='w', index=False,header=["name","product","issue","place","time","taken","coordinate","ID"])
        self.df = pd.read_csv("techissue.csv")
        count=len(self.df)
        self.df = self.df.loc[self.df.ID != self.id, :]
        self.df.to_csv('techissue.csv', mode='w', index=False, header=["ID","customerName","product","issue","location","crit","issueID"])
        print(self.dff)
        print(self.df)
        print("")