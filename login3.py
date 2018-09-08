from tkinter import *
from menu import *
def login():
    n="arial",14,"italic"

    def mcal():
        if var1.get()=="mayank" and password.get()=="12345678":
            loginpage.destroy()
            menu()
        elif var1.get()!="mayank":
            e1.delete(0,len(var1.get()))
            e1.insert(0,"Wrong!!!")
        if password.get()!="12345678":
            e2.delete(0,len(password.get()))
            e2.insert(0,"Wrong!!!")
    loginpage=Tk()
    loginpage.title("login")
    loginpage.geometry("1000x600+0+0")
    var1=StringVar()
    password=StringVar()
    Label(loginpage,text="ENTER NAME",padx=25,width=20,font=(n)).grid(row=0,sticky=W)
    e1=Entry(loginpage,width=25,textvariable=var1)
    e1.grid(row=0,column=1)

    Label(loginpage,text="ENTER PASSWORD",padx=25,width=20,font=(n)).grid(row=1,sticky=W)
    e2=Entry(loginpage,width=25,textvariable=password)
    e2.grid(row=1,column=1)

    Button(loginpage,text="SUBMIT",command=mcal,font=(n),width=20).grid(row=2,column=1)
