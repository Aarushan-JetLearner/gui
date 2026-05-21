from tkinter import *
window=Tk()
window.geometry("400x300")
entry=Entry(window,background="yellow",show="*")
entry.place(x=150,y=125)


entry2=Entry(window,background="yellow")
entry2.place(x=150,y=100)
button=Button(window,text="Enter",background="blue",foreground="blue",bd="10",command=window.destroy)
button.place(x=285,y=100)
label=Label(window,background="blue",text="Enter username")
label.place(x=60,y=100)
label2=Label(window,background="blue",text="Enter password")
label2.place(x=60,y=125)
window.mainloop()