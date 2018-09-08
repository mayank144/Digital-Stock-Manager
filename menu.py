from tkinter import *
from stock import *
from item import *
from SELL import *
from ACCOUNTBOOK import *
from DESCRIPTION import *
from PRICEIN import *
import threading
def menu():
    n="arial",14,"italic"
    menupage=Tk()
    menupage.title("menu")
    menupage.geometry("1000x600+0+0")

    def STOCK():
        menupage.destroy()
        stock()
    def ADDITEM():
        menupage.destroy()
        additem()
    def ACCOUNTBOOk():
        menupage.destroy()
        ACCOUNTBOOK()
    def SELL1():
        menupage.destroy()
        sell()
    def DESCRIPTION():
        menupage.destroy()
        Description()
    def PRICEIn():
        menupage.destroy()
        PRICEIN()
    def PRICEOUt():
        menupage.destroy()
        PRICEOUT()
    def BALANCE():
        price=open("PRICE.txt","r")
        p=price.readline()
        price.close()
        menupage.destroy()
        message("TOTAL BALANCE="+p)
    Button(menupage,text="STOCK",command=STOCK,font=(n),width=20).grid(row=0,column=0)
    Button(menupage,text="ADDITEM",command=ADDITEM,font=(n),width=20).grid(row=1,column=0)
    Button(menupage,text="ACCOUNT BOOK",command=ACCOUNTBOOk,font=(n),width=20).grid(row=2,column=0)
    Button(menupage,text="SELL",command=SELL1,font=(n),width=20).grid(row=3,column=0)
    Button(menupage,text="DESCRIPTION",command=DESCRIPTION,font=(n),width=20).grid(row=4,column=0)
    Button(menupage,text="PRICE IN",command=PRICEIn,font=(n),width=20).grid(row=5,column=0)
    Button(menupage,text="PRICE OUT",command=PRICEOUt,font=(n),width=20).grid(row=6,column=0)
    Button(menupage,text="BALANCE",command=BALANCE,font=(n),width=20).grid(row=6,column=0)
    menupage.mainloop()
    
    t1 = threading.Thread(target=menu)
    t1.start()
    
