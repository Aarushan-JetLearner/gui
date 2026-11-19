from tkinter import *
import random
window=Tk()
window.geometry("500x600")
window.resizable(0,0)
canvas=Canvas(window,width=500,height=600,background="black",bd=0,highlightthickness=0)
canvas.place(x=0,y=0)
p1y1=0
p2y1=0
p1_score=0
p2_score=0
def move_paddle1(event):
    global p1y1
    if event.keysym=="w":
        p1y1=-5
    elif event.keysym=="s":
        p1y1=5
def move_paddle2(event):
    global p2y1
    if event.keysym=="Up":
        p2y1=-5
    elif event.keysym=="Down":
        p2y1=5
def paddle_motion(paddle,change_in_y):
    p=canvas.coords(paddle)
    if p[1]<=0:
        canvas.move(paddle,0,-p[1])
    elif p[3]>=600:
        canvas.move(paddle,0,600-p[3])

    
    canvas.move(paddle,0,change_in_y)
def stop_paddle(event):
    global p1y1,p2y1
    if event.keysym=="w" or event.keysym=="s":
        p1y1=0
    if event.keysym=="Up" or event.keysym=="Down":
        p2y1=0
def loop():
    paddle_motion(paddle1,p1y1)
    paddle_motion(paddle2,p2y1)
    ball_motion()

    window.after(10,loop)

score_paddle1=Label(text=p1_score)
score_paddle1.place(x=230,y=100)
score_paddle2=Label(text=p2_score)
score_paddle2.place(x=260,y=100)
canvas.create_line(250,0,250,600,fill="white")
canvas.create_oval(200,250,300,350,outline="white")
paddle1=canvas.create_rectangle(10,0,25,100,fill="orange",outline="white")
paddle2=canvas.create_rectangle(475,0,490,100,fill="light green",outline="white")
ball=canvas.create_oval(240,290,260,310,fill="yellow",outline="white")
canvas.bind_all("<KeyPress-w>",move_paddle1)
canvas.bind_all("<KeyPress-s>",move_paddle1)
canvas.bind_all("<KeyPress-Up>",move_paddle2)
canvas.bind_all("<KeyPress-Down>",move_paddle2)
canvas.bind_all("<KeyRelease-w>",stop_paddle)
canvas.bind_all("<KeyRelease-s>",stop_paddle)
canvas.bind_all("<KeyRelease-Up>",stop_paddle)
canvas.bind_all("<KeyRelease-Down>",stop_paddle)
list=[4,-4,-4,4]
change_in_x_ball=random.choice(list)
change_in_y_ball=random.choice(list)
def ball_motion():
    global change_in_y_ball,change_in_x_ball,p
    canvas.move(ball,change_in_x_ball,change_in_y_ball)
    ball_cor=canvas.coords(ball)
    paddle1_cor=canvas.coords(paddle1)
    paddle2_cor=canvas.coords(paddle2)
    if ball_cor[1]<=0 or ball_cor[3]>600:
        change_in_y_ball=-change_in_y_ball
    if ball_cor[0]<=0:
        global p2_score,p1_score
        canvas.coords(ball,240,290,260,310)
        change_in_x_ball=random.choice(list)
        change_in_y_ball=random.choice(list)
        p2_score=p2_score+1
        score_paddle2.config(text=f"{p2_score}")
        print(str(p1_score)+"-"+str(p2_score))
    if ball_cor[2]>=500:
        
        canvas.coords(ball,240,290,260,310)
        change_in_x_ball=random.choice(list)
        change_in_y_ball=random.choice(list)
        p1_score=p1_score+1
        score_paddle1.config(text=f"{p1_score}")
        print(str(p1_score)+"-"+str(p2_score))
    if paddle1_cor[0]>ball_cor[0] and paddle1_cor[2]<ball_cor[2] and paddle1_cor[1]<ball_cor[1] and paddle1_cor[3]>ball_cor[3]:
        change_in_x_ball=-change_in_x_ball
    if paddle2_cor[0]>ball_cor[0] and paddle2_cor[2]<ball_cor[2] and paddle2_cor[1]<ball_cor[1] and paddle2_cor[3]>ball_cor[3]:
            change_in_x_ball=-change_in_x_ball

        
        



        





loop()






window.mainloop()