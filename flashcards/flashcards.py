import tkinter as tk
import random

flashcards = [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},
              {'French': 'chercher', 'English': 'search'}, {'French': 'seulement', 'English': 'only'},
              {'French': 'police', 'English': 'police'}, {'French': 'pensais', 'English': 'thought'},
              {'French': 'aide', 'English': 'help'}, {'French': 'demande', 'English': 'request'},
              {'French': 'genre', 'English': 'kind'}, {'French': 'mois', 'English': 'month'},
              {'French': 'frère', 'English': 'brother'}, {'French': 'laisser', 'English': 'let'},
              {'French': 'car', 'English': 'because'}, {'French': 'mettre', 'English': 'to put'},
              {'French': 'aucun', 'English': 'no'}, {'French': 'laisse', 'English': 'leash'},
              {'French': 'eux', 'English': 'them'}, {'French': 'ville', 'English': 'city'},
              {'French': 'chaque', 'English': 'each'}, {'French': 'parlé', 'English': 'speak'},
              {'French': 'arrivé', 'English': 'come'}, {'French': 'devrait', 'English': 'should'},
              {'French': 'bébé', 'English': 'baby'}, {'French': 'longtemps', 'English': 'long time'},
              {'French': 'heures', 'English': 'hours'}, {'French': 'vont', 'English': 'will'},
              {'French': 'pendant', 'English': 'while'}, {'French': 'revoir', 'English': 'meet again'},
              {'French': 'aucune', 'English': 'any'}, {'French': 'place', 'English': 'square'},
              {'French': 'parle', 'English': 'speak'}, {'French': 'compris', 'English': 'understood'},
              {'French': 'savais', 'English': 'knew'}, {'French': 'étaient', 'English': 'were'},
              {'French': 'attention', 'English': 'Warning'}, {'French': 'voici', 'English': 'here is'},
              {'French': 'pourrais', 'English': 'could'}, {'French': 'affaire', 'English': 'case'},
              {'French': 'donner', 'English': 'give'}, {'French': 'type', 'English': 'type'},
              {'French': 'leurs', 'English': 'their'}, {'French': 'donné', 'English': 'given'},
              {'French': 'train', 'English': 'train'}, {'French': 'corps', 'English': 'body'},
              {'French': 'endroit', 'English': 'place'}, {'French': 'yeux', 'English': 'eyes'},
              {'French': 'façon', 'English': 'way'}, {'French': 'écoute', 'English': 'listen'},
              {'French': 'dont', 'English': 'whose'}, {'French': 'trouve', 'English': 'find'},
              {'French': 'premier', 'English': 'first'}, {'French': 'perdu', 'English': 'lost'},
              {'French': 'main', 'English': 'hand'}, {'French': 'première', 'English': 'first'},
              {'French': 'côté', 'English': 'side'}, {'French': 'pouvoir', 'English': 'power'},
              {'French': 'vieux', 'English': 'old'}, {'French': 'sois', 'English': 'be'},
              {'French': 'tiens', 'English': 'here'}, {'French': 'matin', 'English': 'morning'},
              {'French': 'tellement', 'English': 'so much'}, {'French': 'enfant', 'English': 'child'},
              {'French': 'point', 'English': 'point'}, {'French': 'venu', 'English': 'came'},
              {'French': 'suite', 'English': 'after'}, {'French': 'pardon', 'English': 'sorry'},
              {'French': 'venez', 'English': 'come'}, {'French': 'devant', 'English': 'in front of'},
              {'French': 'vers', 'English': 'towards'}, {'French': 'minutes', 'English': 'minutes'},
              {'French': 'demandé', 'English': 'request'}, {'French': 'chambre', 'English': 'bedroom'},
              {'French': 'mis', 'English': 'placed'}, {'French': 'belle', 'English': 'beautiful'},
              {'French': 'droit', 'English': 'law'}, {'French': 'aimerais', 'English': 'would like to'},
              {'French': "aujourd'hui", 'English': 'today'}, {'French': 'mari', 'English': 'husband'},
              {'French': 'cause', 'English': 'cause'}, {'French': 'enfin', 'English': 'finally'},
              {'French': 'espère', 'English': 'hope'}, {'French': 'eau', 'English': 'water'},
              {'French': 'attendez', 'English': 'Wait'}, {'French': 'parti', 'English': 'left'},
              {'French': 'nouvelle', 'English': 'new'}, {'French': 'boulot', 'English': 'job'},
              {'French': 'arrêter', 'English': 'Stop'}, {'French': 'dirait', 'English': 'would say'},
              {'French': 'terre', 'English': 'Earth'}, {'French': 'compte', 'English': 'account'},
              {'French': 'donne', 'English': 'given'}, {'French': 'loin', 'English': 'far'},
              {'French': 'fin', 'English': 'end'}, {'French': 'croire', 'English': 'believe'},
              {'French': 'chérie', 'English': 'sweetheart'}, {'French': 'gros', 'English': 'large'},
              {'French': 'plutôt', 'English': 'rather'}, {'French': 'aura', 'English': 'will have'},
              {'French': 'filles', 'English': 'girls'}, {'French': 'jouer', 'English': 'to play'},
              {'French': 'bureau', 'English': 'office'}]

current_card = {}
score = 0
streak = 0
click_count = 1
how_to_count = 1


def toggle_how_to():
    global how_to_count
    how_to_play.config(state="disabled")
    if how_to_count % 1 == 0:
        canvas.itemconfig(card_title, text="How to play", font=('Helvetica', '40'), fill='#3B322C', justify='center')
        canvas.itemconfig(card_text,
                          text="\n\n\n\n\n\n\n\n\n\n\n\n Wrong           Flip              Start         Check          Correct \nguess          card                               score            guess",
                          font=('Helvetica', '20'), fill='#3B322C')
        how_to_count += 1
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")
        flip_button.config(state="disabled")
        score_button.config(state="disabled")
        start_button.config(state="normal")
    elif canvas.itemcget(card_title, 'text') == "Welcome to":
        how_to_count += 1
        next_card()
    elif canvas.itemcget(card_title, 'text') == "How to play":
        how_to_count += 1
        get_current_card()
    else:
        get_current_card()
        how_to_count += 1
        right_button.config(state="normal")
        wrong_button.config(state="normal")
        flip_button.config(state="normal")
        score_button.config(state="normal")
        how_to_play.config(state="disabled")

def toggle_counter():
    global click_count
    if click_count % 2 == 1:
        show_score()
        click_count += 1
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")
        flip_button.config(state="disabled")
    else:
        get_current_card()
        click_count += 1
        right_button.config(state="normal")
        wrong_button.config(state="normal")
        flip_button.config(state="normal")


def right_answer():
    global score
    global streak
    score += 1
    streak += 1
    next_card()


def wrong_answer():
    global streak
    streak = 0
    next_card()


def get_current_card():
    global current_card
    if canvas.itemcget(card_title, 'text') == "English":
        canvas.itemconfig(card_title, text="English", font=('Helvetica', '40'), fill='white', justify='center')
        canvas.itemconfig(card_text, text=current_card["English"], font=('Helvetica', '60'), fill='white',
                          justify='center')
    else:
        canvas.itemconfig(card_title, text="French", font=('Helvetica', '40'), fill='#3B322C', justify='center')
        canvas.itemconfig(card_text, text=current_card["French"], font=('Helvetica', '60'), fill='#3B322C',
                          justify='center')


def next_card():
    global current_card
    if canvas.itemcget(card_title, 'text') == "English":
        current_card = random.choice(flashcards)
        canvas.itemconfig(card_title, text="English", font=('Helvetica', '40'), fill='white', justify='center')
        canvas.itemconfig(card_text, text=current_card["English"], font=('Helvetica', '60'), fill='white',
                          justify='center')
    else:
        current_card = random.choice(flashcards)
        canvas.itemconfig(card_title, text="French", font=('Helvetica', '40'), fill='#3B322C', justify='center')
        canvas.itemconfig(card_text, text=current_card["French"], font=('Helvetica', '60'), fill='#3B322C',
                          justify='center')

    right_button.config(state="normal")
    wrong_button.config(state="normal")
    score_button.config(state="normal")
    flip_button.config(state="normal")
    start_button.config(state="disabled")
    how_to_play.config(state="normal")


def flip_card():
    if canvas.itemcget(card_title, 'text') == "French":
        canvas.itemconfig(card_title, text="English", font=('Helvetica', '40'), fill='white', justify='center')
        canvas.itemconfig(card_text, text=current_card["English"], font=('Helvetica', '60'), fill='white',
                          justify='center')
        canvas.itemconfig(card_background, image=card_back)
    else:
        canvas.itemconfig(card_title, text="French", font=('Helvetica', '40'), fill='#3B322C', justify='center')
        canvas.itemconfig(card_text, text=current_card["French"], font=('Helvetica', '60'), fill='#3B322C',
                          justify='center')
        canvas.itemconfig(card_background, image=card_front)


def show_score():
    global streak
    canvas.itemconfig(card_title, text="Score", font=('Helvetica', '40'), fill='#3B322C', justify='center')
    if 0 < streak < 2:
        canvas.itemconfig(card_text, text=f"\n\nYour score is {score}\n\nThis could be the start of something "
                                          f"new.\n\nStreak: {streak}",
                          font=('Helvetica', '20'), fill='#3B322C', justify='center')
    elif 1 < streak < 5:
        canvas.itemconfig(card_text, text=f"\n\nYour score is {score}\n\nYou're getting better.\n\nStreak: {streak}",
                          font=('Helvetica', '20'), fill='#3B322C', justify='center')
    elif 4 < streak < 10:
        canvas.itemconfig(card_text, text=f"\n\nYour score is {score}\n\nGood job!\n\nStreak: {streak}",
                          font=('Helvetica', '20'), fill='#3B322C', justify='center')
    elif 9 < streak < 70:
        canvas.itemconfig(card_text, text=f"\n\nYour score is {score}\n\nYou're on a roll!\n\nStreak: {streak}",
                          font=('Helvetica', '20'), fill='#3B322C', justify='center')
    elif streak > 69:
        canvas.itemconfig(card_text, text=f"\n\n\n\nDominique, inique, inique s'en allait tout "
                                          f"simplement\nRoutier pauvre et chantant\nEn tous chemins, "
                                          f"en tous lieux\nIl ne parle que du bon Dieu\nIl ne parle que du bon "
                                          f"Dieu\n\nScore: {score}\nStreak: {streak}", font=('Helvetica', '20'),
                          fill='#3B322C', justify='center')
    elif streak == 0:
        canvas.itemconfig(card_text, text=f"\n\nYour score is {score}", font=('Helvetica', '20'),
                          fill='#3B322C', justify='center')


window = tk.Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg='#B1DDC6')
window.resizable(False, False)

canvas = tk.Canvas(width=800, height=526)
canvas.config(bg='#B1DDC6', highlightthickness=0)
card_back = tk.PhotoImage(file='images/card_back.png')
card_front = tk.PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 158, text='Welcome to', font=('Helvetica', '40'), fill='#3B322C', justify='center')
card_text = canvas.create_text(400, 263, text='Flashcards', font=('Helvetica', '60', 'bold'), fill='#3B322C',
                               justify='center')
canvas.grid(row=0, column=0, columnspan=5)

wrong_image = tk.PhotoImage(file='images/wrong.png')
right_image = tk.PhotoImage(file='images/right.png')

wrong_button = tk.Button(window, image=wrong_image, highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                         activebackground='#B1DDC6', relief="raised", command=wrong_answer)
wrong_button.grid(row=1, column=0)
right_button = tk.Button(window, image=right_image, highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                         activebackground='#B1DDC6', relief="raised", command=right_answer)
right_button.grid(row=1, column=4)

flip_image = tk.PhotoImage(file='images/flip.png')
flip_button = tk.Button(window, image=flip_image, highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                        command=flip_card, activebackground='#B1DDC6')
flip_button.grid(row=1, column=1)

score_image = tk.PhotoImage(file='images/score.png')
score_button = tk.Button(window, image=score_image, text='Score', highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                         command=toggle_counter, activebackground='#B1DDC6')
score_button.grid(row=1, column=3)

start_image = tk.PhotoImage(file='images/start.png')
start_button = tk.Button(window, image=start_image, highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                         command=next_card, activebackground='#B1DDC6')
start_button.grid(row=1, column=2)

how_to_play = tk.Button(window, text='How to play', highlightthickness=2, borderwidth=0, bg='#B1DDC6',
                        activebackground='#B1DDC6', font=('Helvetica', '20', 'bold'), command=toggle_how_to)
how_to_play.grid(row=2, column=0, columnspan=5)

right_button.config(state="disabled")
wrong_button.config(state="disabled")
score_button.config(state="disabled")
flip_button.config(state="disabled")

window.mainloop()
