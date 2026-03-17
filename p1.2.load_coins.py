import turtle as t
from tkinter import PhotoImage
from time import sleep
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
    t.goto(-270 + 150* x,-200)
    t.down()
    #t.goto(-175 + 150* x,-200)
    t.forward(95)
    t.up()

try:
#Load a picture of coin of script
    coin = PhotoImage(file="coin2.png").subsample(10,10)
except:
    coin = PhotoImage(width=1, height=1)

t.addshape("coin",t.Shape("image",coin))
coins = [0]
for i in range(6):
    c = t.Turtle("circle")
    c.shapesize(3)              # make it bigger
    c.color("black", "sky blue")  # black outline, yellow fill
    c = t.Turtle('coin')
    c.up()
    c.goto(-150 + 50 * i,0)
    coins.append(c)
# === REPLACE the whole coin-loading part with this ===
# No image file needed — we draw a simple gold coin with turtle
'''
t.register_shape("mycoin", (
    (0, 40),   # top
    (20, 35), (30, 20), (35, 0),
    (30, -20), (20, -35),
    (0, -40),                  # bottom
    (-20, -35), (-30, -20), (-35, 0),
    (-30, 20), (-20, 35),
    (0, 40)                    # back to top
))

coins = []
for i in range(6):
    c = t.Turtle("mycoin")
    c.color("gold", "yellow")   # border gold, fill yellow
    c.up()
    c.goto(-150 + 50 * i, 0)
    coins.append(c)'''
t.update()
sleep(3)
#Make the coin disappear one at a time
for i in range(6):
    coins[-(i+1)].hideturtle()
    t.update()
    sleep(1)

t.done()
try:
    t.bye()
except t.Terminator:
    pass