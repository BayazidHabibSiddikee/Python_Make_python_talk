import turtle as t
t.Screen()
t.setup(600,500)
t.hideturtle()
t.pensize(5)
t.tracer(False)
t.bgcolor("lavender")
t.title("Guess the word game!")
#How many guess left
scores = 6
#Create a second turtle graphics
left = t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,200)
left.write(f"guess left: {scores}",font = ("ubuntu",16,"normal"))
#Put incorrect guess  on top
t.up()
t.goto(-290,150)
t.write("Incorrect guesses:",font=("Arial",16,"normal"))
#Put four empty boxes for the word to guess
for i in range(4):
    t.goto(-275 + 150* i, -200)
    t.down()
    t.goto(-175 + 150* i, -200)
    t.up()
t.done()
try:
    t.bye()
except t.Terminator:
    pass