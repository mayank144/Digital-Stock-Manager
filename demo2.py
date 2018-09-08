from tkinter import *
from login3 import *
def open():
    new=Tk()
    new.title("Front Page")
    new.geometry("1000x600+0+0")
    profession=[("malik",1),("muneem",2),("exit",3)]
    def malik():
        new.destroy()
        login()
    def muneem():
        new.destroy()
        login()
    def exit():
        new.destroy()
    myLabel1=Label(new,text="Who Are You??",fg="white",bg="red",font=20).grid(row=0,column=0,sticky="w")
    myLabel1=Button(new,text="1.OWNER",fg="white",bg="red",font=20,command=malik).grid(row=1,column=0,sticky="w") 
    myLabel1=Button(new,text="2.SERVICE MAN",fg="white",bg="red",font=20,command=muneem).grid(row=2,column=0,sticky="w") 
    myLabel1=Button(new,text="3.exit",fg="white",bg="red",font=20,command=exit).grid(row=3,column=0,sticky="w")
    new.mainloop()
