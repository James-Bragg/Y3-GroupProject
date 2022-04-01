import sqlite3
from urllib.parse import ParseResultBytes
from pygame_visualizer import *
from main_menu_gui import *
import random
import base64
import hashlib
from cryptography import fernet

#Sqlite3 Commands
conn = sqlite3.connect('SQLDB.sqlite3')
c = conn.cursor() #Initialising cursor
conn.commit()

IDNumbers = ["1","2","3","4","5","6","7","8","9"] #Making ID


#Encryption and decryption
key = 5
alphabet = "abcde5f6g1hi7jklmn8op9q2rs0tuv3wx4yz." + " "
def Encrypt(self): #Very basic encryption
    encrypt = ""
    for i in self:
        pos = alphabet.find(i)
        newpos = (pos + 5) % 38 #Shifts x number of times to encrypt data
        encrypt = encrypt + str(alphabet[newpos])
    return(encrypt)
    
def EventCreate(NumbersList, SortList, ElapsedTime):
    ID = random.choice(IDNumbers)
    for row in range(5):
        ID = ID + random.choice(IDNumbers) #Makes a random ID
    c.execute("SELECT EventID FROM tblMain WHERE EventID = " + '"' +str(ID)+ '"') #SQL for finding ID
    Check = c.fetchone()
    if Check == None: #No rows exist it means no identical ID
        NumbersString = ' '.join([str(x) for x in NumbersList]) #Convert list into a string #Not working yet but close
        NumbersPicked = NumbersString
        AlgorithmPicked = SortList.lower() #Lowers capitals
        Time = str(ElapsedTime) #Value here until we can take time from maingame
        NumberSecure = Encrypt(NumbersPicked)
        AlgorithmSecure = Encrypt(AlgorithmPicked)
        TimeSecure = Encrypt(Time)
        Record = [str(ID), NumberSecure, AlgorithmSecure, TimeSecure] #Puts all details into database
        c.execute("INSERT INTO tblMain VALUES(?,?,?,?)",Record)
        conn.commit()  
    else:
        pass
    

