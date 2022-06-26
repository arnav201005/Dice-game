from tkinter import*
import random
from PIL import ImageTk, Image 
root=Tk()
root.title("Dice Game")
root.configure(background = "blue2") 
root.geometry("500x500")

 
img = ImageTk.PhotoImage (Image.open("dice.jpg"))

player1 = Label(root,text = "player1", bg = "yellow2", fg = "black")
player2 = Label(root,text = "player2", bg = "yellow2", fg = "black")
player1.place(relx = 0.1, rely = 0.4,  anchor = CENTER)
player2.place(relx = 0.9, rely = 0.4,  anchor = CENTER)
score_player1 = Label(root,bg ="yellow2", fg = "black")
score_player2 = Label(root,bg ="yellow2", fg = "black")
score_player1.place(relx = 0.1, rely = 0.5, anchor = CENTER)
score_player2.place(relx = 0.9, rely = 0.5, anchor = CENTER)
dice_random = Label(root,bg = "chocolate1", fg = "white")
dice_random.place(relx = 0.5, rely = 0.5, anchor = CENTER) 
player1_score = 0 

def player1():
    global player1_score
    random_no = random.randit(1,6) 
    dice_random["text"] = "Player1_dice_no : " + str(random_no)
    player1_score = player1_score + random_no
    score_player1["text"] = str(player1_score)
    player1_btn = Button(root,image = img,command = player1) 
    player1_btn.place(relx = 0.1, rely =0.6, anchor = CENTER )

    player2_score = 0

def player2():
    global player2_score
    random_2 = random.randit(1,6) 
    dice_random["text"] = "Player2_dice_no : " + str(random_2)
    player2_score = player2_score + (random_no)
    score_player2["text"] = str(player2_score)
    player2_btn = Button(root,image = img,command = player2)
    player2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)