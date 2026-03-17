import turtle as t
from time import sleep
from random import random
from tkinter import PhotoImage

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
left.goto(-250,200)
left.write(f"Guess left: {score}",font = ("ubuntu",16,"normal"))
# Put incorrect guess  on top
t.up()
t.goto(-250,150)
t.write("Incorrect guesses:", font=("Arial", 16, "normal"))
# Put four empty boxes for the word to guess
for x in range(4):
    t.goto(-270 + 150*x,-200)
    t.down()
    t.forward(95)
    t.up()
    
try:
    coin = PhotoImage(file="coin2.png").subsample(10,10)
except:
    coin = PhotoImage(width=1, height=1)    

t.addshape("coin",t.Shape("image",coin))
coins = []
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
sleep(3)
for i in range(6):
    #coins[-(i+1)].hideturtle()
    circles[-(i+1)].hideturtle()
    t.update()
    sleep(1)

t.done()
try:
    t.bye()
except t.Terminator:
    pass