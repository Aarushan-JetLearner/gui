from tkinter import *
window=Tk()
window.geometry("500x600")
window.resizable(0,0)
canvas=Canvas(window,width=500,height=600,background="black",bd=0,highlightthickness=0)
canvas.place(x=0,y=0)
p1y1=0
p2y1=0
def move_paddle1(event):
    global p1y1
    if event.keysym=="w":
        p1y1=-5
        print("move paddle 1")
    elif event.keysym=="s":
        p1y1=5
        print("move paddle 1")
def move_paddle2(event):
    global p2y1
    if event.keysym=="Up":
        p2y1=-5
    elif event.keysym=="Down":
        p2y1=5
def paddle_motion(paddle,change_in_y):
    canvas.move(paddle,0,change_in_y)
def loop():
    paddle_motion(paddle1,p1y1)
    window.after(10,loop)
    
canvas.create_line(250,0,250,600,fill="white")
canvas.create_oval(200,250,300,350,outline="white")
paddle1=canvas.create_rectangle(0,0,15,100,fill="orange",outline="white")
paddle2=canvas.create_rectangle(485,0,500,100,fill="light green",outline="white")
ball=canvas.create_oval(240,290,260,310,fill="yellow",outline="white")
canvas.bind_all("<KeyPress-w>",move_paddle1)
canvas.bind_all("<KeyPress-s>",move_paddle1)
canvas.bind_all("<KeyPress-Up>",move_paddle2)
canvas.bind_all("<KeyPress-Down>",move_paddle2)
loop()







window.mainloop()