from tkinter import *
import tkinter as tk
import random
import math
import sqlite3

#https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter

#Tinker Commands
root = tk.Tk()
root.title('Algorithm Visualizer')
root.geometry('600x600')

print("hi") #Testing

def ButtonCommit(): #The button to enter information
    global AlgorithmValue, NumbersValue
    AlgorithmValue = str(variable.get()) #Retrieve information from textboxes
    NumbersValue = str(NumbersTextbox.get())
    print(AlgorithmValue) #To see if the inputs are taken in correctly
    print(NumbersValue)
    

SortList = [ "QuickSort", "SomeSort", "TestSort"] #List for options on the different sorts



TopText = Label(root, text = "-------------------------------------" )
FirstText = Label(root, text = "Welcome to the Algorithm Visualizer" )

AlgorithmText = Label(root, text = "Which Algorithm do you want?")
variable = StringVar(root) #Initalisation on the dropdown menu 
variable.set(SortList[0]) # Show default value of dropdown
AlgorithmTextbox = OptionMenu(root, variable, *SortList)

NumbersText = Label(root, text = "What numbers do you want?")
NumbersTextbox = Entry(root, width=10)

CommitButton = Button(root, height=1, width=12, text="Enter", command=lambda: ButtonCommit())






TopText.pack()
FirstText.pack()
AlgorithmText.pack()
AlgorithmTextbox.pack()
NumbersText.pack()
NumbersTextbox.pack()
CommitButton.pack()
root.mainloop()

