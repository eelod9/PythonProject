from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    test = pandas.read_csv("./FlashCard/data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("./FlashCard/data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = test.to_dict(orient='records')

def flip_card():
    canvas.itemconfig(flashcard_img, image=card_back_img )
    canvas.itemconfig(title, text = "English", fill = "white")
    canvas.itemconfig(word, text = current_card["English"],fill = "white" )

def is_known():
    to_learn.remove(current_card)
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("./FlashCard/data/words_to_learn.csv", index=False)

    next_card()

def next_card():
    global current_card, flip_timer,to_learn
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french = current_card["French"]
    english = current_card["English"]
    print(french, english)
    canvas.itemconfig(title, text = "French", fill = "black")
    canvas.itemconfig(word, text = french, fill="black")
    canvas.itemconfig(flashcard_img, image =card_front_img )
    flip_timer = window.after(3000, func= flip_card)

def save_to_file():
    global to_learn
   
    

   #new_card(french, english)



#-----------------------------------UI --------------------------
window = Tk()
window.title("Flashcard App")
window.config(padx= 50, pady= 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR)
card_back_img = PhotoImage(file = "./FlashCard/images/card_back.png" )
card_front_img = PhotoImage(file = "./FlashCard/images/card_front.png" )
#canvas.create_image(400,263,image =card_back_img )
flashcard_img = canvas.create_image(400,263,image =card_front_img )
title = canvas.create_text(400, 150,   font=("Ariel", 40,"italic"))
word = canvas.create_text(400, 263,  font=("Ariel", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
#timer_text = canvas.create_text(103,130, text = "00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row=0, column=0, columnspan= 2)


#timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,35,"bold"),bg=YELLOW)
#timer_label.grid(row=0,column= 1)
wrong_img= PhotoImage(file="./FlashCard/images/wrong.png")
right_img= PhotoImage(file="./FlashCard/images/right.png")

wrong_button= Button(  highlightthickness=0, image = wrong_img,command= next_card)
wrong_button.grid(row=1, column=0)

right_button=  Button(highlightthickness=0, image = right_img, command= is_known)
right_button.grid(row=1, column = 1)
#check_mark_label= Label( fg=GREEN, font=(FONT_NAME,10,"bold"), bg=YELLOW)
#check_mark_label.grid(row=3, column=1)
next_card()
window.mainloop()

