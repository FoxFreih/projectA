import time
import tkinter as tk
from tkinter import ttk
import pandas as pd
import design
def findcrit(product,issue):
    cols=pd.read_csv("IssueTime.csv")
    for i in range(1,len(cols)):
        if(cols["product"][i]==product and cols["discription"][i]==issue):
            return cols["issueLevel"][i]


def readcsv ( num ,file):
    # openning file out of the function
    cols = pd.read_csv(file)
    return cols.iloc[num]
def writetocsv(techID,line):
    #product,issue,location,issueTime,crit
    level=findcrit(line[1],line[2])

    newline={"techID":techID,
             "customerName":line[0],
             "product":line[1],
             "issue":line[2],
             "location":line[3],
             "crit":level}
    df = pd.DataFrame([newline])
    df.to_csv('techissue.csv', mode='a', index=False, header=0)
def shibuts(techID):
    hourCounter=0
    issue=readcsv(3,"customerissue.csv")
    print(type(issue))
    writetocsv(techID,issue)
    return 0
#shibuts(readcsv(2,"UsersList.csv")[0])
