from tkinter import*

top=Tk()
top.geometry("1000x550")
top.title("TEA SHOP BILL")
c=Canvas(top,bg="skyblue",height="550",width="1000")
c.pack()
def can():
    top.destroy()
def tot():
    tea =int(n1.get())
    coffee =int(n2.get())
    samosa =int(n3.get())
    snacks =int(n4.get())

    a=tea*10
    b=coffee*15
    c=samosa*5
    d=snacks*20
    tot=(a+b+c+d)

    
    answer.config(text=tot,font="bold",fg="red",bg="black")
def pri():
    hii = Tk()
    hii.geometry("300x200")
    hii.title("price list")
    l=Label(hii,text="ITEM",font="bold",bd=5,fg="red")
    l.grid(row=0,column=0)
    l=Label(hii,text="                                    ",fg="white",anchor='w')
    l.grid(row=0,column=2)
    l=Label(hii,text="PRICE",font="bold",bd=5,fg="red")
    l.grid(row=0,column=3)
    l=Label(hii,text="TEA",font="bold",bd=5)
    l.grid(row=1,column=0)
    l=Label(hii,text="10",font="bold",bd=5)
    l.grid(row=1,column=3)
    l=Label(hii,text="COFFEE",font="bold",bd=5)
    l.grid(row=2,column=0)
    l=Label(hii,text="15",font="bold",bd=5)
    l.grid(row=2,column=3)
    l=Label(hii,text="SAMOSA",font="bold",bd=5)
    l.grid(row=3,column=0)
    l=Label(hii,text="5",font="bold",bd=5)
    l.grid(row=3,column=3)
    l=Label(hii,text="SNACKS",font="bold",bd=5)
    l.grid(row=4,column=0)
    l=Label(hii,text="20",font="bold",bd=5)
    l.grid(row=4,column=3)
    
  
name=Label(top,text="NAME",fg="black",bg="skyblue",font=("arial",15,"bold"))
name.place(x=50,y=100)
n=Entry(top,width=13,bd=6,bg="pink",fg="black",font=("times",15,"bold"))
n.place(x=120,y=100)


name1=Label(top,text="TEA",fg="black",bg="skyblue",font="bold")
name1.place(x=50,y=150)
n1=Entry(top,width=13,bd=6,bg="yellow",font="bold")
n1.place(x=120,y=150)

name2=Label(top,text="COFFEE",fg="black",bg="skyblue",font="bold")
name2.place(x=50,y=200)
n2=Entry(top,width=13,bd=6,bg="yellow",font="bold")
n2.place(x=130,y=200)

name3=Label(top,text="SAMOSA",fg="black",bg="skyblue",font="bold")
name3.place(x=50,y=250)
n3=Entry(top,width=13,bd=6,bg="yellow",font="bold")
n3.place(x=130,y=250)

name4=Label(top,text="SNACKS",fg="black",bg="skyblue",font="bold")
name4.place(x=50,y=300)
n4=Entry(top,width=13,bd=6,bg="yellow",font="bold")
n4.place(x=130,y=300)

name5=Label(top,text="TOTAL",fg="black",bg="skyblue",font="bold")
name5.place(x=50,y=350)
n5=Entry(top,width=13,bd=6,bg="black",font="bold")
n5.place(x=130,y=350)

bt=Button(top,text="TOTAL",bg="black",fg="red",command=tot,font="bold")
bt.place(x=40,y=450)

bt=Button(top,text="CANCEL",bg="black",fg="red",command=can,font="bold")
bt.place(x=180,y=450)

bt=Button(top,text="GETQr",bg="black",fg="red",font="bold")                                  
bt.place(x=320,y=450)

bt=Button(top,text="PRICE",bg="black",fg="red",font="bold",command=pri)
bt.place(x=460,y=450)

answer=Label(top,text="*",bg="black")
answer.place(x=150,y=355)

top.mainloop()


