from tkinter import *
from datetime import datetime
from message import *
from SHOW import *
def description(PIN,POUT,IIN,IOUT,a):
    description=open('description.txt','a')
    description.write(str(datetime.now())+" || PIN="+str(PIN)+" || POUT="+str(POUT)+" || IIN="+str(IIN)+" || IOUT="+str(IOUT)+" || "+str(a))
    description.close()
    price=open("PRICE.txt","r")
    p=price.readline()
    price.close()
    price=open("PRICE.txt","w")
    price.write(str(PIN-POUT+int(p)))
    price.close()
def Description():
    n="arial",14,"italic"
    Description=Tk()
    Description.title("DESCRIPTION")
    Label(Description,text="ENTER DATE IN FORMAT(yyyy-mm-dd)",font=(n)).grid(row=0,column=0,sticky=W)
    def SEARCH():
        s=var1.get()
        if s[4]!="-" or s[7]!="-":
            message("FORMAT DOES NOT MATCH")
        else:
            Description.destroy()
            description=open('description.txt','r')
            if s in description.read():
                SHOW(s)
            else:
                message("THIS DATE DOES NOT FOUND")
            description.close()
    var1=StringVar()
    e1=Entry(Description,width=25,textvariable=var1)
    e1.grid(row=0,column=1)
    Button(Description,text="SEARCH",command=SEARCH,font=(n)).grid(row=4,column=1)
