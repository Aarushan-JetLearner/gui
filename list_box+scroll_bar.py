from tkinter import *
screen=Tk()
screen.geometry("500x500")
frame=Frame(screen)
frame.place(x=50,y=50)
scrolling=Scrollbar(frame)
scrolling.pack(side=RIGHT,fill=Y)
list_box=Listbox(frame,yscrollcommand=scrolling.set)
scrolling.config(command=list_box.yview)

list_box.pack(side=LEFT)
list_box.insert(END,9,8,7,6,7,3,12,45,7,4,3,6,4,2,7,4,3,7,54,78,5,78,89,34,4)

screen.mainloop()