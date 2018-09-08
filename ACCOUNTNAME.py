from tkinter import *
from message import *
from DESCRIPTION import *
def ACCOUNTNAME(a,x,y,p):
    n="arial",14,"italic"
    accountName=Tk()
    accountName.title("ACCOUNTNAME")
    Label(accountName,text="Your Total Bill="+str(x*y),font=(n)).grid(row=0,sticky=W)
    Label(accountName,text="You Have Paid only="+str(p),font=(n)).grid(row=1,sticky=W)
    Label(accountName,text="Amount Left="+str(x*y-p),font=(n)).grid(row=2,sticky=W)
    Label(accountName,text="ENTER NAME",font=(n)).grid(row=3,sticky=W)
    ACCOUNT=open("ACCOUNT.txt","r")
    account=list(map(str,ACCOUNT.read().split()))
    ACCOUNT.close()
    item=open("item.txt","r")
    quantity=open("quantity.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    item.close()
    quantity.close()
    def makeAccount():
        if var1.get()=="":
            message("ALL FIELDS ARE REQUIRED")
        elif var1.get() not in account:
            accountName.destroy()
            item=open("item.txt","w")
            I[a]-=x
            b=""
            for i in I:
                b=b+str(i)+" "
            item.write(b)
            item.close()
            ACCOUNT=open("ACCOUNT.txt","a")
            ACCOUNT.write(var1.get()+" ")
            ACCOUNT.close()
            message("AMOUNT AND DEAL ACCOUNT HAS BEEN TAKEN and A NEW ACCOUNT with name "+var1.get()+" has been created with balance="+str(x*y-p))
            description(p,0,0,x,"A NEW ACCOUNT CREATE WITH NAME "+var1.get()+" has been created with balance="+str(x*y-p)+"\n")
            PRICE=open("BALANCEPRICE.txt","a")
            PRICE.write(str(x*y-p)+" ")
            PRICE.close()
            acc=open("ACCOUNTNAME.py","a")
            acc.write("    def add"+str(len(account)+1)+"():\n        accountName.destroy()\n        description(p,0,0,x,str(x)+' items of '+Q["+str(len(account))+"]+' is bought by '+account["+str(len(account))+"]+' at the rate of '+str(y)+' per item and he paid only '+str(p)+' INR and now total balance left='+str(x*y-p)+new)\n        price=open('BALANCEPRICE.txt','w')\n        PR["+str(len(account))+"]+=(x*y-p)\n        print(PR["+str(len(account))+"])\n        b=''\n        for i in PR:\n            b=b+str(i)+' '\n        price.write(b+var1.get())\n        message('data saved and Now your balance='+str(PR["+str(len(account))+"]))\n        price.close()\n        item=open('item.txt','w')\n        I[a]-=x\n        b=''\n        for i in I:\n            b=b+str(i)+' '\n        item.write(b)\n        item.close()\n    i+=1\n    Button(accountName,text=account[i],command=add"+str(len(account)+1)+",font=(n),width=20).grid(row=i+5,column=0)\n    Button(accountName,text=PR[i],command=add"+str(len(account)+1)+",font=(n),width=20).grid(row=i+5,column=1)\n")
    var1=StringVar()
    e1=Entry(accountName,width=25,textvariable=var1)
    e1.grid(row=3,column=1)
    Button(accountName,text="Make account",command=makeAccount,font=(n)).grid(row=4,column=1)
    i=-1
    new="\n"
    price=open("BALANCEPRICE.txt","r")
    PR=list(map(int,price.read().split()))
