import sqlite3
from pygame_visualizer import *
from Tkinter import *
import random

#Sqlite3 Commands
conn = sqlite3.connect('SQLDB.sqlite3')
c = conn.cursor() #Initialising cursor
conn.commit()

IDNumbers = ["1","2","3","4","5","6","7","8","9"] #Making ID


def IDCreate():
    ID = random.choice(IDNumbers)
    for row in range(5):
        ID = ID + random.choice(IDNumbers)
        
    SQL = c.execute("SELECT EventID FROM tblMain WHERE EventID = " + '"' +str(ID)+ '"')
    Check = c.fetchone()
    if Check == None: #No rows exist it means no identical ID
        Time = 5 #Value here until we can take time from maingame
        AlgorithmPicked = "Yes" 
        NumbersPicked = "5"
        EventID = ID
        Record = [EventID, NumbersPicked, AlgorithmPicked, Time]
        c.execute("INSERT INTO tblMain VALUES(?,?,?,?)",Record)
        conn.commit()
        
        
    else:
        pass
        

def Encryption():
    pass

def DEncryption(): #Don't really need this
    pass

IDCreate()