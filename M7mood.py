import time
import tkinter as tk
from tkinter import ttk
import pandas as pd
from Funcfile import cal_travel_time
import design
def findcrit(product,issue):
    cols=pd.read_csv("IssueTime.csv")
    for i in range(1,len(cols)):
        if(cols["product"][i]==product and cols["discription"][i]==issue):
            return cols["issueLevel"][i]

def returntime(product,issue):
    count=0
    cols=pd.read_csv("IssueTime.csv")
    for i in range(1,len(cols)):
        if(cols["product"][i]==product and cols["discription"][i]==issue):
            time = cols["time"][i]
            count+=int(time[0:1])*60+int(time[2:])
            return count
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
             "crit":level,
             "issueID":line[-1]}
    df = pd.DataFrame([newline])
    df.to_csv('techissue.csv', mode='a', index=False, header=0)
def shibuts():
    cols = pd.read_csv("UsersList.csv")
    hourCounter = []
    src=[]
    dest=[]
    for i in range( len(cols)):
        src.append([0,0])
        dest.append([0,0])
        hourCounter.append(0)

    col = pd.read_csv("customerissue.csv")
    col2 = col.to_dict()
    i = 0
    for j in range(len(col)):
        issue = readcsv(j, "customerissue.csv")
        if hourCounter[i]+int(returntime(issue[1], issue[2])) < (8 * 60):
            if col2["taken"][j] == 0:
                src[i][0],src[i][1] = dest[i][0],dest[i][1]
                dest[i][0] = float(col["coordinate"][j][1:11])
                dest[i][1] = float(col["coordinate"][j][12:-1])
                if sum(src[i]) != 0:
                    print("time",cal_travel_time(src[i], dest[i]))
                    hourCounter[i] += cal_travel_time(src[i], dest[i])

                hourCounter[i] += returntime(issue[1], issue[2])
                col2["taken"][j] = 1
                techID = cols["ID"][i]
                writetocsv(techID, issue)
        else:
            if sum(hourCounter) <= (8*60)*len(hourCounter):
                j -= 1
        i+=1
        if(i==len(cols)):
            i=0
    print(hourCounter)
    df = pd.DataFrame(col2)
    df.to_csv('customerissue.csv', mode='w',index=False)
    return 0

shibuts()
#print(returntime("laptop","black screen"))