import turtle as t
from time import sleep
from random import choice
from tkinter import PhotoImage,messagebox
import sys

t.Screen()
t.setup(600,500)
t.hideturtle()
t.pensize(5)
t.tracer(False)
t.bgcolor("lavender")
t.title("Guess the word game!")
score = 6
left = t.Turtle()
left.up()
left.hideturtle()
left.goto(-270,200)
left.write(f"Guess left: {score}",font = ("ubuntu",16,"normal"))
# Put incorrect guess  on top
t.up()
t.goto(-270,150)
t.write("Incorrect guesses:", font=("Arial", 16, "normal"))
# Put four empty boxes for the word to guess
for x in range(4):
    t.goto(-270 + 150*x,-200)
    t.down()
    t.forward(95)
    t.up()
    
try:
    coin = PhotoImage(file="coin5.png").subsample(10,10)
except:
    coin = PhotoImage(width=1, height=1)    

t.addshape("coin",t.Shape("image",coin))
#coins = []
circles = []
for i in range(6):
    c = t.Turtle("circle")
    c.shapesize(3)              # make it bigger
    c.color("black", "sky blue")  # black outline, yellow fill
    #coins.append(c)
    #c = t.Turtle('coin')
    c.up()
    c.goto(-150 + 50 * i,0)
    circles.append(c)
    #coin_turtle = t.Turtle('coin')
    #coin_turtle.up()
    #coin_turtle.goto(-150 + 50 * i,0)
    #coins.append(coin_turtle)
t.update()

words = ['that', 'with', 'have', 'this', 'will', 'your', 'from',
        'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time']

word = choice(words)
missed = []
right = []
while True:
    #Take input
    inp = input("Guess a letter (or 'quit' to stop): ").lower()
    if inp == 'quit':
        break
        sys.exit()
    elif inp in list(word):
        for w in range(4):
            if inp == list(word)[w]:
                t.goto(-270 + 150*w,-200)
                t.write(inp.upper(), font=("Arial", 48, "normal"))
                right.append(inp)
        if len(right)==4:
            messagebox.showinfo\
            ("End Game","Great job, you got the word right!")
            sys.exit()
    else:
        missed.append(inp)
        t.goto(-290 + 80 *len(missed),60)
        t.write(inp.upper(), font=("Arial", 24, "normal"))
        score -= 1
        #circles[-(i+1)].hideturtle()
        circles[-(6-score)].hideturtle()
        t.update()
        sleep(1)
        left.clear()
        left.write(f"Guess left: {score}",font = ("ubuntu",16,"normal"))
        if score == 0:
            messagebox.showinfo\
                ("End Game","Sorry, you used up all your six guesses!")
            print(f"You lost! The word was '{word.upper()}'")
            sys.exit()
t.update()

sleep(3)
'''
for i in range(6):
    #coins[-(i+1)].hideturtle()
    circles[-(i+1)].hideturtle()
    t.update()
    sleep(1)'''


t.done()
try:
    t.bye()
except t.Terminator:
    pass