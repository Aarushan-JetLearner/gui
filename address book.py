from tkinter import *
window=Tk()
window.geometry("700x500")
dicti={}
def update_or_add():
    Name1=Name_entry.get()
    if Name1 not in dicti.keys():
        list_box.insert(END,Name1)
    dicti[Name1]=(Address_entry.get(),Birthday_entry.get(),Mobile_entry.get(),Email_entry.get())
    print(dicti)
    




    
Title_Label=Label(window,text="My address book")
Title_Label.place(x=20,y=20)
Open_button=Button(window,text="Open")
Open_button.place(x=200,y=20)
Name=Label(window,text="Name:")
Name.place(x=200,y=100)
Name_entry=Entry(window)
Name_entry.place(x=250,y=100)
Address=Label(window,text="Address:")
Address.place(x=200,y=180)
Address_entry=Entry(window)
Address_entry.place(x=250,y=180)
Mobile=Label(window,text="Mobile:")
Mobile.place(x=200,y=260)
Mobile_entry=Entry(window)
Mobile_entry.place(x=250,y=260)
Email=Label(window,text="Email:")
Email.place(x=200,y=420)
Email_entry=Entry(window)
Email_entry.place(x=250,y=420)
Birthday=Label(window,text="Birthday:")
Birthday.place(x=200,y=340)
Birthday_entry=Entry(window)
Birthday_entry.place(x=250,y=340)
Edit=Button(window,text="Edit")
Edit.place(x=20,y=400)
Delete=Button(window,text="Delete")
Delete.place(x=100,y=400)
Update=Button(window,text="Update/Add",command=update_or_add)
Update.place(x=450,y=400)
Save=Button(window,text="Save")
Save.place(x=200,y=450)
frame=Frame(window)
frame.place(x=50,y=100)
scrollbar=Scrollbar(frame)
scrollbar.pack(side=LEFT,fill=Y)
list_box=Listbox(frame,yscrollcommand=scrollbar.set)
list_box.pack(side=LEFT)

dictionary={}
window.mainloop()
