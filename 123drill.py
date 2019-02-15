import tkinter
from tkinter import *

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


class ParentWindow(Frame):
    
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)

        self.master.geometry('{}x{}'.format(550, 200))
        
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')

        self.varBrowse1 = StringVar()

        self.btnBrowse1 = Button(self.master,text='Browse... ', width=11, height=1, command=self.Browse1)
        self.btnBrowse1.grid(row=1, column=0, padx=(20,0), pady=(20,0))

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, width=50, font=("Times", 12), fg='black', bg='white')   
        self.txtBrowse1.grid(row=1, column=1, padx=(15,0), pady=(15,0), columnspan=2)

        self.btnCloseProgram = Button(self.master, text="Close Program", width=11, height=2, command=self.CloseProgram)
        self.btnCloseProgram.grid(row=3, column=2, padx=(15,0), pady=(15,0), columnspan=3)

    def Browse1(self, title=None, dirName=None):
        fileName = filedialog.askdirectory()
        self.txtBrowse1.insert(0,fileName)
        
    def CloseProgram(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


