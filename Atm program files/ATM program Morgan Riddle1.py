from tkinter import*
from tkinter import ttk
import tkinter.messagebox

class atm:

    def __init__(self, root):
        self.root = root
        self.root.title( "ATM" )
        self.root.geometry("775x760+280+0")
        self.root.configure(background ='gainsboro')

#Borders for the atm#
        MainFrame = Frame(self.root, bd=20, width=760, height=700,relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=6, width=730, height=500, relief=RIDGE)
        TopFrame1.grid(row=1, column =0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=6, width=730, height=500, relief=RIDGE)
        TopFrame2.grid(row=0, column =0, padx=8)

        TopFrame2L = Frame(TopFrame2, bd=5, width=185, height=300, relief=RIDGE)
        TopFrame2L.grid(row=0, column =0, padx=8)
        
        TopFrame2M = Frame(TopFrame2, bd=5, width=195, height=300, relief=RIDGE)
        TopFrame2M.grid(row=0, column =1, padx=8)
        
        TopFrame2R = Frame(TopFrame2, bd=5, width=185, height=300, relief=RIDGE)
        TopFrame2R.grid(row=0, column =2, padx=8)
#Widget#
    #note: self. represents class(what we learned in our zoom meeting)#
        
        self.txtReceipt = Text(TopFrame2M, height = 16, width=42, bd=12, font=('new roman',10,'bold'))
        self.txtReceipt.grid(row=0, column =0)
                    #Buttons Left Side#
        self.img_arrow_L = PhotoImage(file ="E:/Atm program files/arrowL.png")
        
        self.btnArrowL1=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowL2=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowL3=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowL4=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=3, column =0, padx=2, pady =4)

        #These are the arrow buttons for the left side of the atm interface, above this comment ^ #

        self.img_arrow_R = PhotoImage(file ="E:/Atm program files/arrowR.png")

        self.btnArrowR1=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowR2=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowR3=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowR4=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=3, column =0, padx=2, pady =4)

        #These are the arrow buttons for the right of the atm interface, above this comment ^ #


#Number buttons for entering values in the atm#
        self.img1 = PhotoImage(file ="one.png")
        self.btn1=Button(TopFrame1, width=155, height=75, image=self.img1) .grid(row=2, column =0, padx=2, pady =4)
        #Number 1 Button#

        self.img2 = PhotoImage(file ="two.png")
        self.btn2=Button(TopFrame1, width=155, height=75, image=self.img2) .grid(row=2, column =1, padx=2, pady =4)
        #Number 2 Button#

        self.img3 = PhotoImage(file ="three.png")
        self.btn3=Button(TopFrame1, width=155, height=75, image=self.img3) .grid(row=2, column =2, padx=2, pady =4)
        #Number 3 Button#

        self.img4 = PhotoImage(file ="four.png")
        self.btn4=Button(TopFrame1, width=155, height=75, image=self.img4) .grid(row=3, column =0, padx=2, pady =4)
        #Number 4 Button#

        self.img5 = PhotoImage(file ="five.png")
        self.btn5=Button(TopFrame1, width=155, height=75, image=self.img5) .grid(row=3, column =1, padx=2, pady =4)
        #Number 5 Button#
        
        self.img6 = PhotoImage(file ="six.png")
        self.btn6=Button(TopFrame1, width=155, height=75, image=self.img6) .grid(row=3, column =2, padx=2, pady =4)
        #Number 6 Button#
        
        self.img7 = PhotoImage(file ="seven.png")
        self.btn7=Button(TopFrame1, width=155, height=75, image=self.img7) .grid(row=4, column =0, padx=2, pady =4)
        #Number 7 Button#
        
        self.img8 = PhotoImage(file ="eight.png")
        self.btn8=Button(TopFrame1, width=155, height=75, image=self.img8) .grid(row=4, column =1, padx=2, pady =4)
        #Number 8 Button#
        
        self.img9 = PhotoImage(file ="nine.png")
        self.btn9=Button(TopFrame1, width=155, height=75, image=self.img9) .grid(row=4, column =2, padx=2, pady =4)
        #Number 9 Button#

        self.img0 = PhotoImage(file ="zero.png")
        self.btn0=Button(TopFrame1, width=155, height=75, image=self.img0) .grid(row=5, column =1, padx=2, pady =4)
        #Number 0 Button#

        self.imgExit = PhotoImage(file ="Exit.png")
        self.btnExit=Button(TopFrame1, width=155, height=75, image=self.imgExit) .grid(row=4, column =3, padx=2, pady =4)
        #Back or Exit Menu Button#

        self.imgEnter = PhotoImage(file ="Enter.png")
        self.btnEnter=Button(TopFrame1, width=155, height=75, image=self.imgEnter) .grid(row=2, column =3, padx=2, pady =4)
        #Enter Button#

        self.imgCl = PhotoImage(file ="Cl.png")
        self.btnClear=Button(TopFrame1, width=155, height=75, image=self.imgCl) .grid(row=3, column =3, padx=2, pady =4)

     ###########################################################################################################################
        #Entering your pin module#
        def enter_pin():
            pinNu = self.txtReceipt.get("1.0","end-1c")
            if (pinNu == str ("8601")):
                self.txtReceipt.delete ("1.0",END)
        #Types of actions within the ATM#
                self.txtReceipt.insert(END,'\t\t\t ATM' + "\n\n")
                self.txtReceipt.insert(END,'Withdrawl\t\t\t Loan' + "\n\n")
                self.txtReceipt.insert(END,'Receipt\t\t\t Deposit' + "\n\n")
                self.txtReceipt.insert(END,'Balance\t\t\t Request New Pin' + "\n\n")
            
                self.txtReceipt = Text(TopFrame2M, height = 16, width=42, bd=12, font=('new roman',10,'bold'))
                self.txtReceipt.grid(row=0, column =0)
                    
        #Allows user to use the buttons in order to enter ones pin number#          
        
                self.btnArrowL1=Button(TopFrame2L, width=155, height=50, state = NORMAL, image=self.img_arrow_L) .grid(row=0, column =0, padx=2, pady =4)

                self.btnArrowL2=Button(TopFrame2L, width=155, height=50, state = NORMAL, image=self.img_arrow_L) .grid(row=1, column =0, padx=2, pady =4)
        
                self.btnArrowL3=Button(TopFrame2L, width=155, height=50, state = NORMAL, image=self.img_arrow_L) .grid(row=2, column =0, padx=2, pady =4)

                self.btnArrowL4=Button(TopFrame2L, width=155, height=50, state = NORMAL, image=self.img_arrow_L) .grid(row=3, column =0, padx=2, pady =4)

                
                

                self.btnArrowR1=Button(TopFrame2R, width=155, height=50, state = NORMAL, image=self.img_arrow_R) .grid(row=0, column =0, padx=2, pady =4)

                self.btnArrowR2=Button(TopFrame2R, width=155, height=50, state = NORMAL, image=self.img_arrow_R) .grid(row=1, column =0, padx=2, pady =4)
        
                self.btnArrowR3=Button(TopFrame2R, width=155, height=50, state = NORMAL, image=self.img_arrow_R) .grid(row=2, column =0, padx=2, pady =4)

                self.btnArrowR4=Button(TopFrame2R, width=155, height=50, state = NORMAL, image=self.img_arrow_R) .grid(row=3, column =0, padx=2, pady =4)
                
            else:
                self.txtReceipt.delete ("1.0",END)
                self.txtReceipt.insert(END,'Invalid Pin Number' + "\n\n")

            def clear():
                self.txtReceipt = Text(TopFrame2M, height = 16, width=42, bd=12, font=('new roman',10,'bold'))
        self.txtReceipt.grid(row=0, column =0)
                    #Buttons Left Side#
        self.img_arrow_L = PhotoImage(file ="arrowL.png")
        
        self.btnArrowL1=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowL2=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowL3=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowL4=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=3, column =0, padx=2, pady =4)    

        
        self.img_arrow_R = PhotoImage(file ="arrowR.png")

        self.btnArrowR1=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowR2=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowR3=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowR4=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=3, column =0, padx=2, pady =4)

    def insert0():
        value0 = 0
        self.txtReceipt.insert(END,value0)
                
  ################################################Widget###########################################################################      
        self.txtReceipt = Text(TopFrame2M, height = 16, width=42, bd=12, font=('new roman',10,'bold'))
        self.txtReceipt.grid(row=0, column =0)
                    #Buttons Left Side#
        self.img_arrow_L = PhotoImage(file ="arrowL.png")
        
        self.btnArrowL1=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowL2=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowL3=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowL4=Button(TopFrame2L, width=155, height=50, state = DISABLED, image=self.img_arrow_L) .grid(row=3, column =0, padx=2, pady =4)    

        
        self.img_arrow_R = PhotoImage(file ="arrowR.png")

        self.btnArrowR1=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=0, column =0, padx=2, pady =4)

        self.btnArrowR2=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=1, column =0, padx=2, pady =4)
        
        self.btnArrowR3=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=2, column =0, padx=2, pady =4)

        self.btnArrowR4=Button(TopFrame2R, width=155, height=50, state = DISABLED, image=self.img_arrow_R) .grid(row=3, column =0, padx=2, pady =4)

        self.img1 = PhotoImage(file ="one.png")
        self.btn1=Button(TopFrame1, width=155, height=75, image=self.img1) .grid(row=2, column =0, padx=2, pady =4)
        #Number 1 Button#

        self.img2 = PhotoImage(file ="two.png")
        self.btn2=Button(TopFrame1, width=155, height=75, image=self.img2) .grid(row=2, column =1, padx=2, pady =4)
        #Number 2 Button#

        self.img3 = PhotoImage(file ="three.png")
        self.btn3=Button(TopFrame1, width=155, height=75, image=self.img3) .grid(row=2, column =2, padx=2, pady =4)
        #Number 3 Button#

        self.img4 = PhotoImage(file ="four.png")
        self.btn4=Button(TopFrame1, width=155, height=75, image=self.img4) .grid(row=3, column =0, padx=2, pady =4)
        #Number 4 Button#

        self.img5 = PhotoImage(file ="five.png")
        self.btn5=Button(TopFrame1, width=155, height=75, image=self.img5) .grid(row=3, column =1, padx=2, pady =4)
        #Number 5 Button#
        
        self.img6 = PhotoImage(file ="six.png")
        self.btn6=Button(TopFrame1, width=155, height=75, image=self.img6) .grid(row=3, column =2, padx=2, pady =4)
        #Number 6 Button#
        
        self.img7 = PhotoImage(file ="seven.png")
        self.btn7=Button(TopFrame1, width=155, height=75, image=self.img7) .grid(row=4, column =0, padx=2, pady =4)
        #Number 7 Button#
        
        self.img8 = PhotoImage(file ="eight.png")
        self.btn8=Button(TopFrame1, width=155, height=75, image=self.img8) .grid(row=4, column =1, padx=2, pady =4)
        #Number 8 Button#
        
        self.img9 = PhotoImage(file ="nine.png")
        self.btn9=Button(TopFrame1, width=155, height=75, image=self.img9) .grid(row=4, column =2, padx=2, pady =4)
        #Number 9 Button#

        self.img0 = PhotoImage(file ="zero.png")
        self.btn0=Button(TopFrame1, width=155, height=75,command=insert0, image=self.img0) .grid(row=5, column =1, padx=2, pady =4)
        #Number 0 Button#

        self.imgExit = PhotoImage(file ="Exit.png")
        self.btnExit=Button(TopFrame1, width=155, height=75, image=self.imgExit) .grid(row=4, column =3, padx=2, pady =4)
        #Back or Exit Menu Button#

        self.imgEnter = PhotoImage(file ="Enter.png")
        self.btnEnter=Button(TopFrame1, width=155, height=75,command= enter_pin, image=self.imgEnter) .grid(row=2, column =3, padx=2, pady =4)
        #Enter Button#

        self.imgCl = PhotoImage(file ="Cl.png")
        self.btnClear=Button(TopFrame1, width=155, height=75, image=self.imgCl) .grid(row=3, column =3, padx=2, pady =4)

            



       

                



if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
