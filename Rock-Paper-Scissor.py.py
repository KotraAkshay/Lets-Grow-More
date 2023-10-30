from tkinter import *
import random

root = Tk()

root.geometry("400x400")

root.title("Rock Paper Scissor Game")

computer_value = ["Rock", "Paper", "Scissor"]

def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    Player.config(text="Player")
    Comp.config(text="Computer")
    Result.config(text="")

def button_disable():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"

def isrock():
    random_value = computer_value[random.randint(0, 2)]
    if random_value == "Rock":
        game_result = "Match Draw"
    elif random_value == "Scissor":
        game_result = "Player Win"
    else:
        game_result = "Computer Win"
    Result.config(text=game_result)
    Player.config(text="Rock")
    Comp.config(text=random_value)
    button_disable()

def ispaper():
    random_value = computer_value[random.randint(0, 2)]
    if random_value == "Paper":
        game_result = "Match Draw"
    elif random_value == "Scissor":
        game_result = "Computer Win"
    else:
        game_result = "Player Win"
    Result.config(text=game_result)
    Player.config(text="Paper")
    Comp.config(text=random_value)
    button_disable()

def isscissor():
    random_value = computer_value[random.randint(0, 2)]
    if random_value == "Rock":
        game_result = "Computer Win"
    elif random_value == "Scissor":
        game_result = "Match Draw"
    else:
        game_result = "Player Win"
    Result.config(text=game_result)
    Player.config(text="Scissor")
    Comp.config(text=random_value)
    button_disable()

Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

Player = Label(frame, text="Player", padx=40, font=10)
Vs = Label(frame, text="VS", padx=40, font="normal 10 bold")
Comp = Label(frame, text="Computer", padx=40, font=10)

Player.pack(side=LEFT, pady=30)
Vs.pack(side=LEFT, pady=30)
Comp.pack(side=LEFT, pady=30)

Result = Label(root, text="", font="normal 20 bold")

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, bg="pink", command=isrock)
b2 = Button(frame1, text="Paper", font=10, width=7, bg="#6495ED", command=isscissor)
b3 = Button(frame1, text="Scissor", font=10, width=7, bg="lightgreen", command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)
Result.pack(pady=20)

root.mainloop()
