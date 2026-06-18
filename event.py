from tkinter import *

screen=Tk()
result_label = Label(screen, text="", background="grey")
def convert():
    value=entry.get().strip()
    if value == "":
        result_label.config(text="Enter a number")
        return
             

    
    c=float(value)
    f=(c*9/5)+32
    result_label.config(text=f"{f:.2f} °F")
screen.geometry("400x400")
label=Label(screen,text="Celsius->Fahrenheit",background="grey")
label.place(x=150,y=50)
info=Label(screen,text="Temperature in celsius:")
info.place(x=20,y=100)
entry=Entry(screen,background="grey")
entry.place(x=150,y=100)
button=Button(screen,text="convert",command=convert)
button.place(x=150,y=200)
info2_label=Label(screen,text="fahrenheit:")
info2_label.place(x=90,y=300)
result_label.place(x=150,y=300)

screen.mainloop()