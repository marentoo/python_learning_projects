from tkinter import *
import pandas as pd
import random

COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    to_learn_de_data = pd.read_csv("words_to_learn.csv", delimiter=',', encoding='utf-8')
except:
    original_de_data = pd.read_csv("languages/de_pl_180.csv", delimiter=',', encoding='utf-8')
    to_learn = original_de_data.to_dict(orient='records')
else:   
    to_learn = to_learn_de_data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "German",fill= "black")
    canvas.itemconfig(card_word, text = current_card["de"], fill= "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_title, text = "Polish", fill = "white")
    canvas.itemconfig(card_word, text = current_card["pl"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    temp_data = pd.DataFrame(to_learn)
    temp_data.to_csv("words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=10, bg=COLOR)
flip_timer = window.after(3000, func=flip)

#Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")

card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)


#Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image =cross_image, highlightthickness=0,command=next_card )
unknown_button.grid(row = 1, column = 0)

check_image = PhotoImage(file="images/right.png")
unknown_button = Button(image =check_image, highlightthickness=0,command=is_known )
unknown_button.grid(row = 1, column = 2)

flip_image = PhotoImage(file="images/flip.png")
flip_button = Button(image =flip_image, highlightthickness=0,command=flip )
flip_button.grid(row = 1, column = 1)

next_card()

window.mainloop()