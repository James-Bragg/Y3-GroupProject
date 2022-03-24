import sqlite3
from pygame_visualizer import *
from Tkinter import *
import random
import base64
import hashlib
from cryptography import fernet

#Sqlite3 Commands
conn = sqlite3.connect('SQLDB.sqlite3')
c = conn.cursor() #Initialising cursor
conn.commit()

IDNumbers = ["1","2","3","4","5","6","7","8","9"] #Making ID


def EventCreate(NumbersList, SortList, ElapsedTime):
    ID = random.choice(IDNumbers)
    for row in range(5):
        ID = ID + random.choice(IDNumbers)
    SQL = c.execute("SELECT EventID FROM tblMain WHERE EventID = " + '"' +str(ID)+ '"')
    Check = c.fetchone()
    if Check == None: #No rows exist it means no identical ID
        NumbersString = ' '.join([str(x) for x in NumbersList]) #Convert list into a string #Not working yet but close
        NumbersPicked = NumbersString.encode
        AlgorithmPicked = SortList.encode
        Time = str(ElapsedTime).encode #Value here until we can take time from maingame
        NumberSecure = fernet.encrypt(NumbersPicked)
        AlgorithmSecure = fernet.encrypt(AlgorithmPicked)
        TimeSecure = fernet.encrypt(Time)
        Record = [ID, NumberSecure, AlgorithmSecure, TimeSecure]
        c.execute("INSERT INTO tblMain VALUES(?,?,?,?)",Record)
        conn.commit()  
    else:
        pass
    

        

def Encryption():
    pass

def DEncryption(): #Don't really need this
    pass

