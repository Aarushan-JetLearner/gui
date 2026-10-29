from tkinter import *
from tkinter.colorchooser import askcolor
window=Tk()
window.geometry("500x500")
x1=None
y1=None
default_colour="blue"
def activate(button):
    global active_button
    button.config(relief=SUNKEN)
    active_button.config(relief=RAISED)
    active_button=button
    if active_button==eraser:
        global default_colour
        default_colour="white"
    elif active_button==colour:
        default_colour=askcolor(default_colour)[1]
    elif active_button==brush:
        scale.set(10)
    elif active_button==red:
        default_colour="red"
    elif active_button==blue:
        default_colour="blue"
    elif active_button==green:
        default_colour="green"
    elif active_button==yellow:
        default_colour="yellow"
    else:
        default_colour="white"
    
def draw(event):
    global x1,y1
    width=scale.get()

    if x1 and y1:
        canvas.create_line(x1,y1,event.x,event.y,width=width,fill=default_colour,capstyle=ROUND,smooth=True,splinesteps=1000)
    x1=event.x
    y1=event.y

canvas=Canvas(window,width=500,height=400,bg="white")
canvas.bind("<B1-Motion>",draw)

canvas.place(x=0,y=100)
def clear_screen(): 
    canvas.delete("all")
pen=Button(window,text="pen",command=lambda:activate(pen))
pen.place(x=50,y=50)
brush=Button(window,text="brush",command=lambda:activate(brush))
brush.place(x=150,y=50)
colour=Button(window,text="colour",command=lambda:activate(colour))
colour.place(x=250,y=50)
eraser=Button(window,text="eraser",command=lambda:activate(eraser))
eraser.place(x=350,y=50)
scale=Scale(window,from_=1,to=10, orient=HORIZONTAL)
scale.place(x=400,y=30)
active_button=pen
clear_all=Button(window,text="Clear all",command=clear_screen)
clear_all.place(x=350,y=75)
red=Button(window,text="           ",background="red",command=lambda:activate(red))
red.place(x=250,y=80)
blue=Button(window,text="           ",background="blue",command=lambda:activate(blue))
blue.place(x=180,y=80)
yellow=Button(window,text="           ",background="yellow",command=lambda:activate(yellow))
yellow.place(x=110,y=80)
green=Button(window,text="           ",background="green",command=lambda:activate(green))
green.place(x=40,y=80)
window.mainloop()