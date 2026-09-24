from tkinter import *
window=Tk()
window.geometry("500x600")


d={}
def item_add():
    p1=product_name_entry.get()
    if p1 not in d.keys():
        list_box.insert(END,p1)
    d[p1]=(product_id_entry.get(),price_entry.get(),price_entry.get(),quantity_entry.get())
    print(d)
def remove():
    global p1
    p1=product_name_entry.get()
    d.pop(p1)
    print(d)
    list_box.delete(list_box.curselection())
def del_everything():
    d.clear()
    list_box.delete(0,END)

    
title=Label(window,text="Smart inventory manager")
title.place(x=200,y=50)
product_name=Label(window,text="Product name:")
product_name.place(x=50,y=100)
product_id=Label(window,text="Product ID:")
product_id.place(x=50,y=200)
price=Label(window,text="Price($):")
price.place(x=50,y=300)
quantity=Label(window,text="Quantity:")
quantity.place(x=50,y=400)
product_name_entry=Entry(window)
product_name_entry.place(x=135,y=100)
product_id_entry=Entry(window)
product_id_entry.place(x=115,y=200)
price_entry=Entry(window)
price_entry.place(x=100,y=300)
quantity_entry=Entry(window)
quantity_entry.place(x=105,y=400)
add_item_entry=Button(window,text="Add item",command=item_add)
add_item_entry.place(x=115,y=500)
delete=Button(window,text="Delete",command=remove)
delete.place(x=250,y=500)
clear=Button(window,text="Clear",command=del_everything)
clear.place(x=385,y=500)
frame=Frame(window)
frame.place(x=350,y=100)
scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=Y)
list_box=Listbox(frame,yscrollcommand=scrollbar.set)
list_box.pack(side=RIGHT)

window.mainloop()