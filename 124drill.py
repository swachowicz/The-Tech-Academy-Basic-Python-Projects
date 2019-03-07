#browse buttons
import tkinter
from tkinter import *

from tkinter import filedialog

#create database
import sqlite3
import os, sys

#cut, paste
import shutil

#fPath
import os.path, time

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(450, 200))
        
        self.master.title('Check files')
        self.master.config(bg='#F0F0F0')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
        self.varBrowse3 = StringVar()

        self.btnBrowse1 = Button(self.master,text='Source Directory... ', width=20, height=1, command=self.Browse1)
        self.btnBrowse1.grid(row=1, column=0, padx=(20,0), pady=(20,0))
            
        self.btnBrowse2 = Button(self.master,text='Destination Directory... ', width=20, height=1, command=self.Browse2)
        self.btnBrowse2.grid(row=2, column=0, padx=(15,0), pady=(15,0))

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, width=30, font=("Times", 12), fg='black', bg='white')   
        self.txtBrowse1.grid(row=1, column=1, padx=(15,0), pady=(15,0), columnspan=2)

        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, width=30, font=("Times", 12), fg='black', bg='white')
        self.txtBrowse2.grid(row=2, column=1, padx=(15,0), pady=(15,0), columnspan=2)

        self.btnTransferFiles = Button(self.master, text="Transfer Text Files...", width=16, height=2, command=self.TransferFiles)
        self.btnTransferFiles.grid(row=3, column=0, padx=(15,0), pady=(15,0))

        self.btnCloseProgram = Button(self.master, text="Close Program", width=12, height=2, command=self.CloseProgram)
        self.btnCloseProgram.grid(row=3, column=2, padx=(15,0), pady=(15,0), columnspan=2)


    def Browse1(self, title=None, dirName=None):
        fileName = filedialog.askdirectory()
        self.txtBrowse1.insert(0,fileName)

    def Browse2(self, title=None, dirName=None):
        fileName = filedialog.askdirectory()
        self.txtBrowse2.insert(0,fileName)
        
    def TransferFiles(self, title=None, dirName=None):
        def create_connection(db_file):
            try:
                conn = sqlite3.connect(db_file)
                print(sqlite3.version)
            except Error as e:
                print(e)
            finally:
                conn.close()

        if __name__ == '__main__':
            create_connection("C:\\C\pythonsqlite2.db")
          
        conn = sqlite3.connect('pythonsqlite2.db')

        #   create tbl_TextDocs

        with conn:
            #cur = cursor, operates on actual database
            cur = conn.cursor()
            #sql code in string w/ integer primary key autoincrement
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_TextDocs( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_name TEXT \
                )")
            conn.commit()
        conn.close()

        fPath = self.varBrowse1.get() 

        items = os.listdir(fPath)
        
        destination = self.varBrowse2.get()

        newlist = []
        for names in items:
            if names.endswith(".txt"):
                newlist.append(names)
                abPath = os.path.join(fPath, names)
                
                print(names, "last modified time : ",time.ctime(os.path.getmtime(abPath)))

                

                conn = sqlite3.connect('pythonsqlite2.db')

                with conn:
                    #cur = cursor, operates on actual database
                    cur = conn.cursor()
                    #sql code in string
                    cur.execute("INSERT INTO tbl_TextDocs(col_name) VALUES (?)", \
                                [names])
                    conn.commit()
                conn.close()     
                shutil.move(abPath,destination)
                
     
    def CloseProgram(self):
        self.master.destroy()



    

if __name__ == "__main__":
    #instantiating Tkinter & the class, & named it root
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
