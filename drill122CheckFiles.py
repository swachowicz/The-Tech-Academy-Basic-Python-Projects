
import tkinter
from tkinter import *
# import * for "all"


class ParentWindow(Frame):
        #arguments & keyword arguments
        #def __init__ (self, master, **args, **kwargs):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
                                #resizing width and height of the window of the program, False = don't resize
                                #telling it to resize w/ True
                                #self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(450, 200))
                                #700 pixels wide, 400 pixels height
        
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')
            #bg = background
            #self.master.config(bg='#000') #black

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
      
                #fg=foreground
                #lbl = label
                #pack -- stacks rows or boxes on top of each other
                #grid -- looks more professional
                # txt for textbox, var for variable
                # Entry is basic, one line text box
                #colspan = 2, automatically goes as 1 if not specified

        self.btnBrowse1 = Button(self.master,text='Browse... ', width=11, height=1, command=self.Browse1)
        self.btnBrowse1.grid(row=1, column=0, padx=(20,0), pady=(20,0))
            
        self.btnBrowse2 = Button(self.master,text='Browse... ', width=11, height=1, command=self.Browse2)
        self.btnBrowse2.grid(row=2, column=0, padx=(15,0), pady=(15,0))

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, width=30, font=("Times", 12), fg='black', bg='white')   
        self.txtBrowse1.grid(row=1, column=1, padx=(15,0), pady=(15,0), columnspan=2)

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, width=30, font=("Times", 12), fg='black', bg='white')
        self.txtBrowse2.grid(row=2, column=1, padx=(15,0), pady=(15,0), columnspan=2)

        self.btnCheckFiles = Button(self.master, text="Check for files...", width=11, height=2, command=self.CheckFiles)
        self.btnCheckFiles.grid(row=3, column=0, padx=(15,0), pady=(15,0))

        self.btnCloseProgram = Button(self.master, text="Close Program", width=11, height=2, command=self.CloseProgram)
        self.btnCloseProgram.grid(row=3, column=2, padx=(15,0), pady=(15,0), columnspan=2)

    def Browse1(self):
        bI = self.varBrowse1.get()

    def Browse2(self):
        bII = self.varBrowse2.get()

    def CheckFiles(self):
        bI = self.varBrowse1.get()
        bII = self.varBrowse2.get()
        
    def CloseProgram(self):
        self.master.destroy()

if __name__ == "__main__":
    #instantiating Tkinter & the class, & named it root
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


