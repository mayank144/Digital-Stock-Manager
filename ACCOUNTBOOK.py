from tkinter import *
from message import *
from SUBMITMONEY import *
def ACCOUNTBOOK():
    n="arial",14,"italic"
    accountBook=Tk()
    accountBook.title("ACCOUNTBOOK")
    Label(accountBook,text="ENTER S.no.:",font=(n)).grid(row=0,sticky=W)
    ACCOUNT=open("ACCOUNT.txt","r")
    account=list(map(str,ACCOUNT.read().split()))
    ACCOUNT.close()
    price=open("BALANCEPRICE.txt","r")
    PR=list(map(int,price.read().split()))
    price.close()
    def NEXT():
        if var1.get()>=1 and var1.get()<=len(account):
            accountBook.destroy()
            SUBMITMONEY(var1.get()-1)
        else:
            message("NOT VALID S.no.")
    var1=IntVar()
    e1=Entry(accountBook,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    Button(accountBook,text="NEXT",command=NEXT,font=(n)).grid(row=1,column=1)
    Label(accountBook,text="S.no.:",font=(n)).grid(row=2,sticky=W)
    Label(accountBook,text="ACCOUNT HOLDERNAME",font=(n)).grid(row=2,column=1,sticky=W)
    Label(accountBook,text="ACCOUNT BALANCE LEFT",font=(n)).grid(row=2,column=2,sticky=W)
    for i in range(len(account)):
        Label(accountBook,text=str(i+1),font=(n)).grid(row=3+i,column=0,sticky=W)
        Label(accountBook,text=account[i],font=(n)).grid(row=3+i,column=1,sticky=W)
        Label(accountBook,text=str(PR[i]),font=(n)).grid(row=3+i,column=2,sticky=W)
