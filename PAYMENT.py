from tkinter import *
from message import *
from ACCOUNTNAME import *
from DESCRIPTION import *
def payment(a,x,y):
    n="arial",14,"italic"
    BILL=Tk()
    BILL.title("BILL")
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    def des():
        BILL.destroy()
    def LEFT():
        BILL.destroy()
        item=open("item.txt","r")
        I=list(map(int,item.read().split()))
        item.close()
        if I[a]<x:
            item=open("item.txt","w")
            message("NOT AVAILABLE")
            b=""
            for i in I:
                b=b+str(i)+" "
            item.write(b)
            item.close()
        elif var1.get()>=x*y:
            item=open("item.txt","w")
            I[a]-=x
            b=""
            for i in I:
                b=b+str(i)+" "
            item.write(b)
            item.close()
            message("AMOUNT AND DEAL HAS BEEN TAKEN")
            description(var1.get(),0,0,str(x),str(x)+" number of "+Q[a]+" has been sold for "+str(x*y)+" INR ("+str(y)+" per unit)\n")
        if var1.get()<x*y:
            ACCOUNTNAME(a,x,y,var1.get())
    var1=IntVar()
    var2=IntVar()
    Label(BILL,text="YOUR BILL",font=(n)).grid(row=0,sticky=W)
    Label(BILL,text="S.no.",font=(n)).grid(row=1,sticky=W)
    Label(BILL,text="Item Name",font=(n)).grid(row=1,column=1,sticky=W)
    Label(BILL,text="Quantity",font=(n)).grid(row=1,column=2,sticky=W)
    Label(BILL,text="price",font=(n)).grid(row=1,column=3,sticky=W)
    Label(BILL,text="1.",font=(n)).grid(row=2,sticky=W)
    Label(BILL,text=Q[a],font=(n)).grid(row=2,column=1,sticky=W)
    Label(BILL,text=str(x),font=(n)).grid(row=2,column=2,sticky=W)
    Label(BILL,text=str(y),font=(n)).grid(row=2,column=3,sticky=W)
    Label(BILL,text="TOTAL BILL",font=(n)).grid(row=3,sticky=W)
    Label(BILL,text="--------",font=(n)).grid(row=3,column=1,sticky=W)
    Label(BILL,text=str(x*y),font=(n)).grid(row=3,column=2,sticky=W)
    Label(BILL,text="AMOUNT PAID",font=(n)).grid(row=4,column=0,sticky=W)
    e1=Entry(BILL,width=25,textvariable=var1)
    e1.grid(row=4,column=1)
    Label(BILL,text="AMOUNT LEFT",font=(n)).grid(row=5,column=0,sticky=W)
    #e2=Label(BILL,width=25,font=(n),text=var1.get())
    #e2.grid(row=5,column=1)
    def CALCULATE():
        Label(BILL,text=str(x*y-var1.get()),font=(n)).grid(row=5,column=2,sticky=W)
    Button(BILL,text="CALCULATE",command=CALCULATE,font=(n)).grid(row=5,column=1)
    Button(BILL,text="AMOUNT HAS BEEN PAID",command=LEFT,font=(n)).grid(row=6,column=0)
    Button(BILL,text="BACK",command=des,font=(n),width=20).grid(row=7,column=0)
