from tkinter import *
from message import *
from presentitem import *
from DESCRIPTION import *
def additem():
    n="arial",14,"italic"
    def BACK1():
        additem.destroy()
    additem=Tk()
    additem.title("additem")
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    def add():
        if var1.get()=="" or var2.get()==0:
            message("ALL Fields are required")
        elif var1.get() not in Q:
            """item=open("item.txt","w")
            quantity=open("quantity.txt","w")
            for i in range(len(Q)):
                if var1.get()==Q[i]:
                    I[i]=int(var2.get())+int(I[i])
                    break
            a=""
            b=""
            for i in I:
                a=a+str(i)+" "
            for i in Q:
                b=b+i+" "
            item.write(a)
            quantity.write(b)
            additem.destroy()
            message("data saved")
            item.close()
            quantity.close()
        else:"""
            item=open("item.txt","w")
            quantity=open("quantity.txt","w")
            a=""
            b=""
            for i in I:
                a=a+str(i)+" "
            for i in Q:
                b=b+i+" "
            item.write(a+str(var2.get()))
            quantity.write(b+var1.get())
            additem.destroy()
            message("data saved")
            item.close()
            quantity.close()
            file=open("SELL.py","a")
            file.write('\n    def SELL'+str(len(I)+1)+'():\n        sellpage.destroy()\n        SELL('+str(len(I))+')\n    i+=1\n    var'+str(len(I)+1)+'=IntVar()\n    Button(sellpage,text=str(i)+".\t"+Q[i-1]+"\t"+str(I[i-1]),command=SELL'+str(len(I)+1)+',font=(n),width=20).grid(row=i+1,column=0)')
            file.close()
            item=open("item.py","a")
            item.write("\n    def add"+str(len(I)+1)+"():\n        additem.destroy()\n        presentitem("+str(len(I))+")\n    i+=1\n    Button(additem,text=Q[i],command=add"+str(len(I)+1)+",font=(n),width=20).grid(row=i+4,column=0)")
            item.close()
            description(0,0,var2.get(),0,str(var2.get())+" number of "+var1.get()+"(new item) added\n")
    
    var1=StringVar()
    var2=IntVar()
    Label(additem,text="Enter Name",padx=25,width=10,font=(n)).grid(row=0,sticky=W)
    e1=Entry(additem,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    Label(additem,text="Enter Quantity",padx=25,width=10,font=(n)).grid(row=1,sticky=W)
    e2=Entry(additem,width=25,textvariable=var2)
    e2.grid(row=1,column=1)
    Button(additem,text="ADD",command=add,font=(n),width=20).grid(row=2,column=1)
    Button(additem,text="BACK",command=BACK1,font=(n),width=20).grid(row=2,column=0)
    i=-1

