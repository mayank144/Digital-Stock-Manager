from tkinter import *
def stock():
    n="arial",14,"italic"
    st=Tk()
    def BACK2():
        st.destroy()
    st.title("stock")
    quantity=open("quantity.txt","r")
    item=open("item.txt","r")
    I=list(map(int,item.read().split()))
    Q=list(map(str,quantity.read().split()))
    i=0
    while i<len(I):
        Label(st,text=Q[i],padx=25,width=10,font=(n)).grid(row=i,column=0,sticky=W)
        Label(st,text=str(I[i]),padx=25,width=10,font=(n)).grid(row=i,column=1,sticky=W)
        i+=1
    Button(st,text="BACK",command=BACK2,font=(n),width=20).grid(row=i+1,column=0)
    quantity.close()
    item.close()

