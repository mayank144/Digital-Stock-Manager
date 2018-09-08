from tkinter import *
from PAYMENT import *
def SELL(a):
    n="arial",14,"italic"
    sellItem=Tk()
    sellItem.title("sellitem")
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    def NEXT():
        sellItem.destroy()
        payment(a,var1.get(),var2.get())
    var1=IntVar()
    var2=IntVar()
    Label(sellItem,text="S.no.\tItem Name\tAvailable",font=(n)).grid(row=0,sticky=W)
    Label(sellItem,text="Quantity\t\t",font=(n)).grid(row=0,column=1,sticky=W)
    Label(sellItem,text="price",font=(n)).grid(row=0,column=2,sticky=W)
    Label(sellItem,text="1.\t"+Q[a]+"\t\t"+str(I[a])+"\t",font=(n)).grid(row=1,sticky=W)
    e1=Entry(sellItem,width=25,textvariable=var1)
    e1.grid(row=1,column=1)
    e2=Entry(sellItem,width=25,textvariable=var2)
    e2.grid(row=1,column=2)
    Button(sellItem,text="NEXT",command=NEXT,font=(n),width=20).grid(row=3,column=0)
