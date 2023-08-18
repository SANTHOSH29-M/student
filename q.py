from tkinter import*
import qrcode

top=Tk()
top.title("QRcode")
top.geometry("1000x550")
top.resizable(False,False)

def form():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")

    global Image
    Image=PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(top)
Image_view.pack(padx=50,pady=10,side=RIGHT)

name=Label(top,text="name").place(x=50,y=170)
title=Entry(top,width=13)
title.place(x=50,y=200)

entry=Entry(top,width=28)
entry.place(x=50,y=250)

genarate=Button(top,text="genarate",width=20,height=2,bg="black",fg="red",command=form).place(x=50,y=300)

top.mainloop()
