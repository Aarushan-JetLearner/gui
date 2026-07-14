from tkinter import *
from tkinter.filedialog import *
screen=Tk()
screen.geometry("400x300")
def open_file():

    file_store=askopenfile(title="txtfile")
    list_box.delete(0,END)
    read=file_store.readlines()
    for i in read:
        list_box.insert(END,i)

def deletion():
    list_box.delete(list_box.curselection())
    
def data_save():
    file_name_store=asksaveasfile(defaultextension=".txt")
    for i in list_box.get(0,END):
        print(i,file=file_name_store)
    list_box.delete(0,END)
def adding():
    list_box.insert(END,entry.get())
    
open=Button(screen,text="Open",command=open_file)
open.place(x=100,y=50)
delete=Button(screen,text="Delete",command=deletion)
delete.place(x=200,y=50)
save=Button(screen,text="Save",command=data_save)
save.place(x=300,y=50)
add=Button(screen,text="Add",command=adding)
add.place(x=350,y=200)
frame=Frame(screen)
frame.place(x=10,y=75)
scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)


list_box=Listbox(frame,yscrollcommand=scrollbar.set)
list_box.pack(side=LEFT)
for i in range(100):
    list_box.insert(END,"List "+str(i+1))
scrollbar.config(command=list_box.yview)
entry=Entry(screen,text="")
entry.place(x=270,y=150)
screen.mainloop()