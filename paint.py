from tkinter import *
window=Tk()
window.geometry("500x500")

def activate(button):
    global active_button
    button.config(relief=SUNKEN)
    active_button.config(relief=RAISED)
    active_button=button
canvas=Canvas(window,width=500,height=400,bg="blue")
canvas.place(x=0,y=100)
pen=Button(window,text="paint",command=lambda:activate(pen))
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
window.mainloop()