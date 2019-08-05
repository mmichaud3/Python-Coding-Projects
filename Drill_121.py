import tkinter
from tkinter import *




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.txtBrowse1 = Entry(self.master, text=self.varBrowse1, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=3, column=1, rowspan=1,  columnspan=5, padx=(30,40), pady=(30,0))

        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, font=("Helvetica", 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=4,  column=1, rowspan=1, columnspan=6, padx=(30,40), pady=(30,0))

        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(30,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse2.grid(row=4, column=0, padx=(30, 0), pady=(30, 0))

        self.btnCheckFiles = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnCheckFiles.grid(row=5, column=0, padx=(30,0), pady=(30,0))

        self.btnClose = Button(self.master, text="Close Program",width=15, height=2)
        self.btnClose.grid(row=5, column=5, padx=(0,30), pady=(30,0))







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

