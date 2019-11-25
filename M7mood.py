import time
import tkinter as tk
from tkinter import ttk
import pandas as pd
import design
def readcsv ( num ):
    # openning file out of the function
    cols = pd.read_csv("customerissue.csv")
    return cols.iloc[num]
def shibuts():
    
    return 0

