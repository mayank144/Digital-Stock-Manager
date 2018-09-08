from tkinter import *
from demo2 import *
def close():
    front.destroy()

def open1():
    front.destroy()
    open()

front=Tk()
front.title("Front Page")
front.geometry("1000x600+0+0")
myLabel1=Label(front,text="WELCOME DIGITAL STOCK MANAGER",fg="white",bg="red",font=20).grid(row=0,column=0,sticky="w") 
myLabel2=Label(front,text="DO you want to continue(y/n)",fg="red",bg="yellow",font=10).grid(row=1,column=0,sticky="w") 
myButton1=Button(front,text="yes",fg="red",bg="white",font=10,command= open1).grid(row=2,column=0,sticky="w")
myButton2=Button(front,text="no",fg="red",bg="white",font=10,command= close).grid(row=2,column=1,sticky="w")
front.mainloop()
