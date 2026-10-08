from tkinter import *
import random
from tkinter import messagebox
window=Tk()
window.geometry("400x600")
word_choice=""
score=0
def word_gen():
    global word_choice
    words=["algorithm","wave","candle","cut","pointificate"]
    word_choice=random.choice(words)
    word_choice_list=list(word_choice)
    random.shuffle(word_choice_list)
    jumbled_word="".join(word_choice_list)
    Word.config(text=jumbled_word)
def answer_check():
    global score
    Ans=Enter.get()
    if Ans==word_choice:
        score=score+1
        score2.config(text="Score: "+str(score))
        Enter.delete(0,END)
        Word.config(text="Word")
    else:
        messagebox.showinfo("Game over","Game over")
        score=0
        score2.config(text="Score: "+str(score))


Title=Label(window,text="Jumbled word game")
Title.place(x=150,y=50)
Word=Label(window,text="Word")
Word.place(x=150,y=200)
Enter=Entry(window)
Enter.place(x=150,y=300)
Answer_check=Button(window,text="Check answer",command=answer_check)
Answer_check.place(x=150,y=400)
Generate=Button(window,text="Generate",command=word_gen)
Generate.place(x=150,y=250)
score2=Label(window,text="Score")
score2.place(x=350,y=500)
window.mainloop()