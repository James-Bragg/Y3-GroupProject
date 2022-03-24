from tkinter import *
import tkinter as tk
import xdrlib
from PIL import ImageTk, Image #pip install pillow
import sqlite3

# constants
n_height = 560
n_width = 480

cr_back = '#1d2a48'
cr_white = '#FFFFFF'
cr_text = '#fff'
cr_button = '#48fee7'
cr_bg_text = '#0c171d'
str_title = 'Algorithm Visualizer'

root = tk.Tk()
root.title(str_title)
root.geometry('{}x{}'.format(n_width, n_height))
root.mainloop()

#These are the variables to be passed into SQL
NumbersList = [] #List to append numbers into
SortList = ""

conn = sqlite3.connect('SQLDB.sqlite3')
c = conn.cursor() #Initialising cursor
conn.commit()

sql = "SELECT * FROM tblMain"
sql =c.execute("SELECT * FROM tblMain")
rows = c.fetchall()


i=1
e = Label(root,width=10, text="ID", borderwidth=2,relief='ridge', anchor="w") 
e.grid(row=i,column=j)
for data in sql: 
    for j in range(len(data)):
        e = Entry(root, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        #e.insert(END, data[j])
    i=i+1






#Tinker Commands
#This is where the code starts