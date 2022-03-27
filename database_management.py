import sqlite3
from pygame_visualizer import *
from Tkinter import *
import random
import base64


#Sqlite3 Commands
conn = sqlite3.connect('SQLDB.sqlite3')
c = conn.cursor() #Initialising cursor
conn.commit()

IDNumbers = ["1","2","3","4","5","6","7","8","9"] #Making ID

#def Encryption(self):
 #       password = self.encode("utf-8")
  #      encoded = base64.b64encode(password)
    #    return encoded

def EventCreate(NumbersList, SortList, ElapsedTime):
    ID = random.choice(IDNumbers)
    for row in range(5):
        ID = ID + random.choice(IDNumbers)
    SQL = c.execute("SELECT EventID FROM tblMain WHERE EventID = " + '"' +str(ID)+ '"')
    Check = c.fetchone()
    if Check == None: #No rows exist it means no identical ID
        Time = str(ElapsedTime) #Value here until we can take time from maingame
        AlgorithmPicked = SortList
        NumbersString = ' '.join([str(x) for x in NumbersList]) #Convert list into a string
        NumbersPicked = NumbersString
        Record = [ID, NumbersPicked, AlgorithmPicked, Time]
        c.execute("INSERT INTO tblMain VALUES(?,?,?,?)",Record)
        conn.commit()  
    else:
        pass
        

def Encryption():
    pass

def DEncryption(): #Don't really need this
    pass

