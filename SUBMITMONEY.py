from tkinter import *
from message import *
from DESCRIPTION import *
def SUBMITMONEY(a):
    n="arial",14,"italic"
    submitMoney=Tk()
    submitMoney.title("SUBMIT MONEY")
    ACCOUNT=open("ACCOUNT.txt","r")
    account=list(map(str,ACCOUNT.read().split()))
    ACCOUNT.close()
    price=open("BALANCEPRICE.txt","r")
    PR=list(map(int,price.read().split()))
    price.close()
    def NEXT():
        submitMoney.destroy()
        PR[a]=PR[a]-var1.get()
        price=open("BALANCEPRICE.txt","w")
        for i in range(len(PR)):
            price.write(str(PR[i])+" ")            
        price.close()
        message(str(var1.get())+" INR has been deposited to account="+account[a]+" and now "+str(PR[a])+" INR balance has been left")
        description(var1.get(),0,0,0,str(var1.get())+" INR has been deposited to account="+account[a]+" and now "+str(PR[a])+" INR balance has been left\n")
    Label(submitMoney,text="ACCOUNT HOLDER NAME",font=(n)).grid(row=0,sticky=W)
    Label(submitMoney,text="ACCOUNT BALANCE",font=(n)).grid(row=1,sticky=W)
    Label(submitMoney,text="HOW MUCH MONEY DO YOU WANT DEPOSIT",font=(n)).grid(row=2,sticky=W)
    Label(submitMoney,text=account[a],font=(n)).grid(row=0,column=1,sticky=W)
    Label(submitMoney,text=PR[a],font=(n)).grid(row=1,column=1,sticky=W)
    var1=IntVar()
    e1=Entry(submitMoney,width=25,textvariable=var1)
    e1.grid(row=2,column=1)
    Button(submitMoney,text="NEXT",command=NEXT,font=(n)).grid(row=3,column=1)
