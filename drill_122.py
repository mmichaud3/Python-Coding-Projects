

from tkinter import *
import tkinter.filedialog
import tkinter as tk





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.askDir1 = StringVar()

        self.askDir1 = Entry(self.master, text=self.askDir1, font=("Helvetica", 12), fg='black', bg='white')
        self.askDir1.grid(row=3, column=1, columnspan=5, padx=(30, 40), pady=(30, 0))


        self.askDir = Button(self.master, text="Search...", width=15, height=1, command=lambda : onSelect(self))
        self.askDir.grid(row=3, column=0, padx=(30, 0), pady=(30, 0))

def onSelect(self):
    fileName = tkinter.filedialog.askdirectory()
    self.askDir1.insert(0, fileName)











if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
