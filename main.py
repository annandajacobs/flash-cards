import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
atual_card = {} 
para_aprender = {}

try:
    dados = pandas.read_csv("./projeto/projeto16/data/palavras_para_aprender.csv")
except FileNotFoundError:
    dados_originais = pandas.read_csv("./projeto/projeto16/data/french.csv")
    para_aprender = dados_originais.to_dict(orient="records")
else:  
    para_aprender = dados.to_dict(orient="records")

def next_card():
    global atual_card, passar_tempo
    window.after_cancel(passar_tempo)
    atual_card = random.choice(para_aprender)
    canvas.itemconfig(card_titulo, text="Francês", fill="black")
    canvas.itemconfig(card_palavra, text=atual_card["Francês"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    passar_tempo = window.after(3000, func=girar_card)

def girar_card():
    canvas.itemconfig(card_titulo, text="Português", fill="white")
    canvas.itemconfig(card_palavra, text=atual_card["Português"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_know():
    para_aprender.remove(atual_card)
    dados = pandas.DataFrame(para_aprender)
    dados.to_csv("./projeto/projeto16/data/palavras_para_aprender.csv", index=False)
    next_card()

# ----------------- UI SETUP --------------------
window = Tk()
window.title("Flash Cards em Francês")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

passar_tempo = window.after(3000, func=girar_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./projeto/projeto16/image/card_front.png")
card_back_img = PhotoImage(file="./projeto/projeto16/image/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_titulo = canvas.create_text(400, 150, text="título", font=("Ariel", 40, "italic"))
card_palavra = canvas.create_text(400, 263, text="Palavra", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

botao_erro_img = PhotoImage(file="./projeto/projeto16/image/wrong.png")
botao_erro = Button(image=botao_erro_img, highlightthickness=0, command=next_card)
botao_erro.grid(column=0, row=1)

botao_check_img = PhotoImage(file="./projeto/projeto16/image/right.png")
botao_check = Button(image=botao_check_img, highlightthickness=0, command=is_know)
botao_check.grid(column=1, row=1)

next_card()

window.mainloop()
