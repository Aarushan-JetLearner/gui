from tkinter import *
screen=Tk()
screen.geometry("400x400")
dicti={}
def read_name():
    global dicti
    Name3=Name2.get()
    dicti[Name3]=True
    print(dicti)
def erase():
    global Name3
    Name3=Name2.get()
    dicti.pop(Name3)
    print(dicti)
def iteration():
    for i in dicti:
        print(i)
        print(dicti[i])
Name=Button(screen,text="Name")
Name.place(x=50,y=20)
Name2=Entry(screen)
Name2.place(x=95,y=25)
Enter=Button(screen,text="Enter",command=read_name)
Enter.place(x=180,y=20)
Remove=Button(screen,text="Remove",command=erase)
Remove.place(x=220,y=20)
Iterate=Button(screen,text="Iterate",command=iteration)
Iterate.place(x=200,y=200)
screen.mainloop()
