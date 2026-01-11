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
    RepeatCheck = None
    RepeatVar = None
    frequencyInput = None


    def __init__(self):
        super().__init__()
        self.title('EEG data streamer')
        #self.geometry('500x150')

        self.quit_button = tk.Button(self, text="Quit", command=sys.exit)
        self.quit_button.grid(row=3, column=0, sticky=tk.E)

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.grid(row=3, column=1, sticky=tk.E)

        self.load_file_button = tk.Button(self, text="Select File", command=self.load_file)
        self.load_file_button.grid(row=0, column=0, sticky=tk.E)

        self.load_file_button = tk.Label(self, text="")
        self.load_file_button.grid(row=0, column=1, sticky=tk.E)

        self.RepeatVar = tk.IntVar()
        self.checkButton = tk.Checkbutton(self, text = 'Repeat', variable = self.RepeatVar, onvalue = 1, offvalue = 0)
        self.checkButton.grid(row=1, column=0, sticky=tk.E)

        tk.Label(self, text='Frequency').grid(row=2, column=0, sticky=tk.E)
        self.frequencyInput = tk.Entry(self)
        self.frequencyInput.grid(row=2, column=1, sticky=tk.E)
        self.frequencyInput.delete(0, tk.END)
        self.frequencyInput.insert(0, '512')



    def start(self):
        self.file_holder.set_file_path(self.file)
        self.file_holder.set_repeat(bool(self.RepeatVar.get()))
        self.file_holder.set_fs(int(self.frequencyInput.get().strip()))

        self.quit()



    def load_file(self):
        self.file = filedialog.askopenfile(mode='r').name
        self.load_file_button.config(text= self.file)



    def set_file_holder(self, file_holder):
        self.file_holder = file_holder
