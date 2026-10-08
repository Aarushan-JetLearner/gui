from tkinter import *
screen=Tk()
screen.geometry("402x402")
variable="x"
def player(choice):
    global variable
    choice["text"]=variable
    if variable=="x":
        variable="o"
    elif variable=="o":
        variable="x"
    

    
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