from tkinter import*
from tkinter import messagebox

top=Tk()
top.geometry("800x720")
top.config(bg="lightsalmon1")
top.resizable(False,False)

tops=Frame(top,bg="lightskyblue2",width=1600,height=150,bd=10,relief=SUNKEN)
tops.pack(side=TOP)

title=Label(tops,text="STUDENT INFORMATION SYSTEM",bg="lightskyblue2",font=('times',30,'bold'),fg="black")
title.place(x=50,y=40)

label=Label(tops,font="bold",text="__________________________________________________________________________",fg="black",bg="lightskyblue2")
label.place(x=50,y=80)

sn=Label(top,text="STUDENT NANE ",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sn.place(x=50,y=180)

sr=Label(top,text="ROLL NUMBER  ",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sr.place(x=50,y=250)

sc=Label(top,text="CLASS ",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sc.place(x=50,y=310)

sm1=Label(top,text="MARK1",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sm1.place(x=50,y=370)

sm1=Label(top,text="MARK2",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sm1.place(x=50,y=430)

sp=Label(top,text="PERCENTAGE",bg="lightsalmon1",font=('times',20,'bold'),fg="black")
sp.place(x=50,y=490)

sb=Button(top,text="SUBMIT",bg="black",fg="red",font=('times',20,'bold'))
sb.place(x=50,y=600)

sb=Button(top,text="CANCEL",bg="black",fg="red",font=('times',20,'bold'))
sb.place(x=520,y=610)

e1=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e1.place(x=400,y=180)

e2=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e2.place(x=400,y=250)

e3=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e3.place(x=400,y=310)

e4=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e4.place(x=400,y=370)

e5=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e5.place(x=400,y=430)

e6=Entry(top,font=('algerian',20,'bold'),bg="lightpink2",justify="center",bd=6)
e6.place(x=400,y=490)

top.mainloop()

