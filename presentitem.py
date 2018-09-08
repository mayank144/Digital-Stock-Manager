from tkinter import *
from message import *
from DESCRIPTION import *
def presentitem(a):
    n="arial",14,"italic"
    presentItem=Tk()
    presentItem.title("PRESENT ITEM")
    var1=IntVar()
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    Label(presentItem,text="Enter Quantity for "+Q[a],font=(n)).grid(row=0,sticky=W)
    e1=Entry(presentItem,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    def add():
        if var1.get()==0:
            message("ALL Fields are required")
        else:
            item=open("item.txt","w")
            I[a]=int(var1.get())+int(I[a])
            b=""
            for i in I:
                b=b+str(i)+" "
            item.write(b)
            presentItem.destroy()
            message("data saved")
            item.close()
            description(0,0,var1.get(),0,str(var1.get())+" more number of "+Q[a]+" added\n")
    Button(presentItem,text="ADD",command=add,font=(n),width=20).grid(row=2,column=1)
    Button(presentItem,text="BACK",command=presentItem.destroy,font=(n),width=20).grid(row=3,column=0)
