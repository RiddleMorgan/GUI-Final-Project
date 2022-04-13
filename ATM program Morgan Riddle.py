from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm:

    def __init__(self, root):
        self.root = root
        #blank_space = " "
        #self.root.title(110 *blank_space + "ATM"
        self.root.title( "ATM" )
        self.root.geometry("774x760+280+0")
        self.root.configure(background ='gainsboro')

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
