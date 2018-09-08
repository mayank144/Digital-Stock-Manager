from tkinter import *
from DESCRIPTION import *
def PRICEIN():
    n="arial",14,"italic"
    PRICEIN=Tk()
    PRICEIN.title("PRICEIN")
    Label(PRICEIN,text="ENTER AMOUNT",font=(n)).grid(row=0,column=0,sticky=W)
    def NEXT():
        PRICEIN.destroy()
        message(str(var1.get())+" INR is given by "+var2.get())
        description(var1.get(),0,0,0,var2.get()+"\n")
    var1=IntVar()
    e1=Entry(PRICEIN,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    Label(PRICEIN,text="ENTER REASON",font=(n)).grid(row=1,column=0,sticky=W)
    var2=StringVar()
    e2=Entry(PRICEIN,width=25,textvariable=var2)
    e2.grid(row=1,column=1)
    Button(PRICEIN,text="I HAVE TAKEN MONEY",command=NEXT,font=(n)).grid(row=2,column=1)
def PRICEOUT():
    n="arial",14,"italic"
    PRICEOUT=Tk()
    PRICEOUT.title("PRICEOUT")
    Label(PRICEOUT,text="ENTER AMOUNT",font=(n)).grid(row=0,column=0,sticky=W)
    def NEXT():
        PRICEOUT.destroy()
        message(str(var1.get())+" INR given to  "+var2.get())
        description(0,var1.get(),0,0,var2.get()+"\n")
    var1=IntVar()
    e1=Entry(PRICEOUT,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    Label(PRICEOUT,text="ENTER REASON",font=(n)).grid(row=1,column=0,sticky=W)
    var2=StringVar()
    e2=Entry(PRICEOUT,width=25,textvariable=var2)
    e2.grid(row=1,column=1)
    Button(PRICEOUT,text="I HAVE GIVEN MONEY",command=NEXT,font=(n)).grid(row=2,column=1)
