from tkinter import *
import tkinter as tk
import random
import math
import sqlite3

#Tinker Commands
root = tk.Tk()
root.title('Algorithm Visualizer')
root.geometry('600x600')

def ButtomCommit(): #The button to enter information
    AlgorithmValue = AlgorithmTextbox.get()
    NumbersValue = NumbersTextbox.get()
    print(AlgorithmValue)
    print(NumbersValue)
    

OPTIONS = [ "QuickSort", "Test", "Test"] #List for options on the different sorts
variable = StringVar(root) #Initalisation on the dropdown menu 
variable.set(OPTIONS[0]) # Show default value of dropdown



TopText = Label(root, text = "-------------------------------------" )
FirstText = Label(root, text = "Welcome to the Algorithm Visualizer" )

AlgorithmText = Label(root, text = "Which Algorithm do you want?")
AlgorithmTextbox = OptionMenu(root, variable, *OPTIONS)

NumbersText = Label(root, text = "What numbers do you want?")
NumbersTextbox = Entry(root, width=10)







TopText.pack()
FirstText.pack()
AlgorithmText.pack()
AlgorithmTextbox.pack()
NumbersText.pack()
NumbersTextbox.pack()
root.mainloop()

