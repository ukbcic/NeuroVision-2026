import sys
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk


class MainUI(tk.Tk):

    file = None
    start_button = None
    quit_button = None
    file_label = None
    load_file_button = None
    file_holder = None


    def __init__(self):
        super().__init__()
        self.title('EEG data streamer')
        #self.geometry('500x150')

        self.quit_button = tk.Button(self, text="Quit", command=sys.exit)
        self.quit_button.grid(row=1, column=3, sticky=tk.E)

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.grid(row=1, column=2, sticky=tk.E)

        self.load_file_button = tk.Button(self, text="Select File", command=self.load_file)
        self.load_file_button.grid(row=0, column=0, sticky=tk.E)

        self.load_file_button = tk.Label(self, text="")
        self.load_file_button.grid(row=0, column=1, sticky=tk.E)



    def start(self):
        self.file_holder.set_file_path(self.file)
        self.quit()

    def load_file(self):
        self.file = filedialog.askopenfile(mode='r').name
        self.load_file_button.config(text= self.file)


    def set_file_holder(self, file_holder):
        self.file_holder = file_holder
