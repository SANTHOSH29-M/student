from tkinter import*
from gtts import gTTS,gTTSError
from playsound import playsound


root = Tk()
root.geometry("890x580+0+0")
root.title("CONVERT TEXT TO AUDIO")
root.config(bg="aquamarine1")

Tops = Frame(root,bg="black",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

Tops1 = Frame(root,bg="black",width = 1600,height=50,relief=SUNKEN)
Tops1.pack(side=BOTTOM)

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="CONVERT TEXT TO AUDIO",fg="Black",bg="lightseagreen",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

lblinf = Label(Tops1, font=( 'aria' ,30, 'bold' ),text="SHY BOY CONVERTER",fg="Black",bg="lightseagreen",bd=10,anchor='w')
lblinf.grid(row=0,column=0)

label=Label(root,text="ENTER THE TEXT",font="arial 15 bold",bg="aquamarine1")
label.place(x=340,y=150)

msg = StringVar()

entry=Entry(root,textvariable =msg,width=50,bd=6,bg="azure3")
entry.place(x=250,y=180,width=380,height=70)

def speech():
    message = entry.get()
    speech = gTTS(text = message)
    speech.save("shyboy.mp3")
    playsound("shyboy.mp3")

def cancel():
    root.destroy()

def again():
    msg.set("")

play=Button(root, text = "PLAY" , font = 'arial 15 bold', command = speech, width =6,bd=4,bg="red",fg="black")
play.place(x=250,y=300)

can=Button(root, text = "CANCEL" , font = 'arial 15 bold', command = cancel, width =6,bd=4,bg="red",fg="black")
can.place(x=380,y=300)

ag=Button(root, text = "TRY AGAIN" , font = 'arial 15 bold', command = again, width =10,bd=4,bg="red",fg="black")
ag.place(x=500,y=300)

root.mainloop()

