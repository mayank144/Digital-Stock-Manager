from tkinter import *
def SHOW(s):
    n="arial",14,"italic"
    SHOW=Tk()
    SHOW.title("Description Show")
    Label(SHOW,text="DESCRIPTION OF DATE("+s+")",font=(n)).grid(row=0,column=0,sticky=W)
    description=open('description.txt','r')
    a=description.readline()
    i=1
    while a!="":
        if a[0:10]==s:
            Label(SHOW,text=a[:-1]).grid(row=i,column=0,sticky=W)
        a=description.readline()
        i+=1
    description.close()
