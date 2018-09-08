from tkinter import *
from SELL2 import *
"""from tkinter import *
from SELL2 import *
def sell():
    n="arial",14,"italic"
    sellpage=Tk()
    sellpage.title("sell")
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    var=[0 for i in range(len(I))]
    def SELL1():
        sellpage.destroy()
        SELL2(var)
    quantity.close()
    def ADD():
        var[0]=var1.get()
        var[1]=var2.get()
        var[2]=var3.get()
        print(var)
    Label(sellpage,text="S.No\tITEM NAME   Quantity",font=(n)).grid(row=0,sticky=W)
    var1=IntVar()
    i=0
    Checkbutton(sellpage,text=str(i+1)+".\t"+Q[i]+"\t"+str(I[i]),variable=var1,indicatoron=0,command=ADD,font=(n),width=20).grid(row=1,column=0)
    var2=IntVar()
    i+=1
    Checkbutton(sellpage,text=str(i+1)+".\t"+Q[i]+"\t"+str(I[i]),variable=var2,indicatoron=0,command=ADD,font=(n),width=20).grid(row=2,column=0)
    var3=IntVar()
    i+=1
    Checkbutton(sellpage,text=str(i+1)+".\t"+Q[i]+"\t"+str(I[i]),variable=var3,indicatoron=0,command=ADD,font=(n),width=20).grid(row=3,column=0)
    Button(sellpage,text="NEXT",command=SELL1,font=(n),width=20).grid(row=i+2,column=0)
"""
def sell():
    n="arial",14,"italic"
    sellpage=Tk()
    sellpage.title("sell")
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    var=[0 for i in range(len(I))]
    def NEXT():
        print(var)
    i=0
    Label(sellpage,text="S.No\tITEM NAME   Quantity",font=(n)).grid(row=i,sticky=W)

    
