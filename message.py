from tkinter import *
def message(a):
    n="arial",14,"italic"
    def BACK():
        message.destroy()
    message=Tk()
    message.title("message")
    Label(message,text=a,font=(n)).grid(row=0,column=0,sticky=W)
    Button(message,text="BACK",command=BACK,font=(n),width=20).grid(row=1,column=0)
