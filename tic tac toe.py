from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.geometry("402x402")
variable="x"
def player(choice):
    global variable
    if choice["text"]=="":
        choice["text"]=variable
        variable="o"
        if choice["text"]=="o":
            variable="x"
    if Button1["text"]!="" and Button1["text"]==Button2["text"]==Button3["text"]:
        messagebox.showinfo("You win",Button1["text"]+" win")
        disable_buttons()
    elif Button4["text"]!="" and Button4["text"]==Button5["text"]==Button6["text"]:
        messagebox.showinfo("You win",Button4["text"]+ " win")
        disable_buttons()
    elif Button7["text"]!="" and Button7["text"]==Button8["text"]==Button9["text"]:
        messagebox.showinfo("You win",Button7["text"]+" win")
        disable_buttons()
    if Button1["text"]!="" and Button1["text"]==Button4["text"]==Button7["text"]:
        messagebox.showinfo("You win",Button1["text"]+" win")
        disable_buttons()
    elif Button2["text"]!="" and Button2["text"]==Button5["text"]==Button8["text"]:
        messagebox.showinfo("You win",Button2["text"]+" win")
        disable_buttons()
    elif Button3["text"]!="" and Button3["text"]==Button6["text"]==Button9["text"]:
        messagebox.showinfo("You win",Button3["text"]+" win")
        disable_buttons()
    elif Button1["text"]!="" and Button1["text"]==Button5["text"]==Button9["text"]:
        messagebox.showinfo("You win",Button1["text"]+" win")
        disable_buttons()
    elif Button3["text"]!="" and Button3["text"]==Button5["text"]==Button7["text"]:
        messagebox.showinfo("You win",Button3["text"]+" win")
        disable_buttons()

def disable_buttons():
    Button1.config(state=DISABLED)
    Button2.config(state=DISABLED)
    Button3.config(state=DISABLED)
    Button4.config(state=DISABLED)
    Button5.config(state=DISABLED)
    Button6.config(state=DISABLED)
    Button7.config(state=DISABLED)
    Button8.config(state=DISABLED)
    Button9.config(state=DISABLED)


    

    
Button1=Button(screen,text="",command=lambda:player(Button1))
Button1.place(x=0,y=0,width=134,height=134)
Button2=Button(screen,text="",command=lambda:player(Button2))
Button2.place(x=134,y=0,width=134,height=134)
Button3=Button(screen,text="",command=lambda:player(Button3))
Button3.place(x=268,y=0,width=134,height=134)
Button4=Button(screen,text="",command=lambda:player(Button4))
Button4.place(x=0,y=134,width=134,height=134)
Button5=Button(screen,text="",command=lambda:player(Button5))
Button5.place(x=134,y=134,width=134,height=134)
Button6=Button(screen,text="",command=lambda:player(Button6))
Button6.place(x=268,y=134,width=134,height=134)
Button7=Button(screen,text="",command=lambda:player(Button7))
Button7.place(x=0,y=268,width=134,height=134)
Button8=Button(screen,text="",command=lambda:player(Button8))
Button8.place(x=134,y=268,width=134,height=134)
Button9=Button(screen,text="",command=lambda:player(Button9))
Button9.place(x=268,y=268,width=134,height=134)


screen.mainloop()