from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

# constants
n_height = 560
n_width = 480

cr_back = '#1d2a48'
cr_text = '#fff'
cr_button = '#48fee7'
cr_bg_text = '#0c171d'

str_title = 'Algorithm Visualizer'

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        sort_list = ["QuickSort", "SomeSort", "TestSort"]  # List for options on the different sorts
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
        self.algorithm = StringVar(self.master)  # Initialisation on the dropdown menu
        self.algorithm.set(sort_list[0])  # Show default value of dropdown
        algorithm_textbox = OptionMenu(self.master, self.algorithm, *sort_list)
        algorithm_text.configure(background=cr_back, font=("Comic Sans MS", 10, "bold"), fg=cr_text)
        algorithm_textbox.configure(borderwidth=0, font=("Comic Sans MS", 12, "bold"))

        txt_numbers = Label(self.master, text="What numbers do you want?", font=("Comic Sans MS", 10, "bold"))
        txt_numbers.configure(background=cr_back, fg=cr_text, borderwidth=0)
        self.numbers_box = Entry(self.master, width=10, font=12)
        self.numbers_box.configure(background=cr_bg_text, fg=cr_text)

        commit_button = Button(self.master, height=1, width=12, text="Enter", command=self.commit, font=("Comic Sans MS", 10, "bold"))
        commit_button.configure(background=cr_button, borderwidth=0, )

        img = ImageTk.PhotoImage(Image.open('./1.png'))
        label = Label(self.master, image = img)
        label.img = img
        label.configure(borderwidth=0)

        first_text.pack(in_=title_frame, side=LEFT)
        second_text.pack(in_=title_frame, side=RIGHT)
        title_frame.pack(pady=20)
        algorithm_text.pack(pady=5)
        algorithm_textbox.pack(pady=5)
        txt_numbers.pack(pady=5)
        self.numbers_box.pack(pady=5)
        commit_button.pack(pady=10)
        label.pack(pady=10)

    def commit(self):  # The button to enter information

        algorithm_value = str(self.algorithm.get())  # Retrieve information from textboxes
        numbers_value = str(self.numbers_box.get())
        print(algorithm_value)
        print(numbers_value)


# https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
# Tinker Commands
root = tk.Tk()
root.title(str_title)
root.geometry('{}x{}'.format(n_width, n_height))
root.configure(background=cr_back)
app = Application(master=root)
app.mainloop()
