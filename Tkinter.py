from tkinter import *
from pygame_visualizer import *
import tkinter as tk
import xdrlib
from PIL import ImageTk, Image #pip install pillow
from DBViewer import *
from tkinter import filedialog

# constants
n_height = 840
n_width = 720

cr_back = '#1d2a48'
cr_white = '#FFFFFF'
cr_text = '#fff'
cr_button = '#48fee7'
cr_bg_text = '#0c171d'
str_title = 'Algorithm Visualizer'

#These are the variables to be passed into SQL
NumbersList = [] #List to append numbers into
SortList = ""


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        sort_list = ["Quick Sort", "Bubble Sort", "Insertion Sort"]  # List for options on the different sorts
        # Font_tuple = ("Comic Sans MS", 20, "bold")

        title_frame = Frame(self.master)
        first_text = Label(title_frame,
                           text="Welcome to,",

                           font=("Comic Sans MS", 15, "bold")
                           , fg=cr_text, background=cr_back)
        second_text = Label(title_frame,
                           text=str_title,
                           font=("Comic Sans MS", 15, "bold"), fg=cr_button, background=cr_back)


        algorithm_text = Label(self.master, text="Which Algorithm do you want?")
        self.algorithm = StringVar(self.master)  # Initialiation on the dropdown menu
        self.algorithm.set(sort_list[0])  # Show default value of dropdown
        algorithm_textbox = OptionMenu(self.master, self.algorithm, *sort_list)
        algorithm_text.configure(background=cr_back, font=("Comic Sans MS", 10, "bold"), fg=cr_text)
        algorithm_textbox.configure(borderwidth=0, font=("Comic Sans MS", 12, "bold"))

        txt_numbers = Label(self.master, text="What numbers do you want?", font=("Comic Sans MS", 10, "bold"))
        txt_numbers.configure(background=cr_back, fg=cr_text, borderwidth=0)
        #self.numbers_box = Entry(self.master, width=10, font=12)
        #self.numbers_box.configure(background=cr_bg_text, fg=cr_text)

        commit_button = Button(self.master, height=1, width=12, text="Input Number", command=self.commitnumber, font=("Comic Sans MS", 10, "bold"))
        commit_button.configure(background=cr_white, borderwidth=0, )
                
        self.wrong_text = Label(self.master, text="    ")
        self.wrong_text.configure(background=cr_back, font=("Comic Sans MS", 10, "bold"), fg=cr_text)
        
        self.list_text = Label(self.master, text="    ")
        self.list_text.configure(background=cr_back, font=("Comic Sans MS", 10, "bold"), fg=cr_text)
        
        
        finalcommit_button = Button(self.master, height=2, width=15, text="Confirm", command=self.commitfinal, font=("Comic Sans MS", 10, "bold"))
        finalcommit_button.configure(background=cr_button, borderwidth=0, )
        
        DB_button = Button(self.master, height=2, width=15, text="View Database", command=self.DBCommit, font=("Comic Sans MS", 10, "bold"))
        DB_button.configure(background=cr_button, borderwidth=0, )

        img = ImageTk.PhotoImage(Image.open('./1.png'))
        label = Label(self.master, image = img)
        label.img = img
        label.configure(borderwidth=0)

        #All of these below is the order they show in
        first_text.pack(in_=title_frame, side=LEFT)
        second_text.pack(in_=title_frame, side=RIGHT)
        title_frame.pack(pady=20)
        algorithm_text.pack(pady=5)
        algorithm_textbox.pack(pady=5)
        txt_numbers.pack(pady=5)
        #self.numbers_box.pack(pady=5)
        commit_button.pack(pady=10)
        self.wrong_text.pack(pady=5)
        self.list_text.pack(pady=5)
        finalcommit_button.pack(pady=10)
        DB_button.pack(pady=10)
        label.pack(pady=10)
        
    def commitnumber(self):  # The button to enter information 
        try:
            txt = filedialog.askopenfilename()
            with open(""+txt) as file:
                NumbersList = [NumbersList.rstrip('\n') for NumbersList in file]
                NumbersList = list(map(int,NumbersList))
            self.wrong_text.configure(text="")
            #numbers_value = self.numbers_box.get() # Retrieve information from textboxes
            #self.numbers_box.delete(0, END)
            #NumbersList.append(int(numbers_value))
            for x in NumbersList:
                self.list_text.config(text=repr(NumbersList))
            print(NumbersList)
        except:
            #self.numbers_box.delete(0, END)
            self.wrong_text.configure(text="Please enter a number")
            print("error")
  
    def commitfinal(self):
        algorithm_value = str(self.algorithm.get())
        SortList = algorithm_value #Make initial sortlist to be passed into different script
        sort_list = ["Quick Sort", "Bubble Sort", "Insertion Sort"]

            
        print(NumbersList)
        print(algorithm_value)
        main(NumbersList, SortList)

    def DBCommit(self):
        Commit()
    
#Tinker Commands
#This is where the code starts
def start():
    root = tk.Tk()
    root.title(str_title)
    root.geometry('{}x{}'.format(n_width, n_height))
    root.configure(background=cr_back)
    app = Application(master=root)
    app.mainloop()
