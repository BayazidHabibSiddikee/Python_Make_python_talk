import turtle as t
from time import sleep
from random import choice
from tkinter import PhotoImage, messagebox
import sys
import arrow

# -------------------------
#  WORD LIST
# -------------------------
words = [
    "nice","want","have","need","wish","give","take","love","care","help",
    "hold","keep","know","send","make","find","feel","look","show","move",
    "live","stay","join","play","work","read","talk","hear","plan","hope",
    "deal","lead","grow","rise","fall","meet","save","open","shut","turn",
    "stop","wait","walk","jump","rest","pick","push","pull","pack","pass",
    "sign","test","call","cook","bake","wash","boil","flip","stir","pour",
    "peel","feed","lift","sort","draw","type","edit","sing","snap","film",
    "zoom","chat","mail","link","code","load","sync","view","copy","clip",
    "text","post","roll","spin","calm","kind","fair","good","fine","pure",
    "true","easy","fast","slow","soft","hard","busy","cool","warm","mild",
    "bold","cute","neat","sure","okay","able","just","even","else","only",
    "some","many","more","less","most","ever","once","then","when","soon",
    "later","here","away","down","back","over","into","onto","from","with",
    "amid","upon","near","side","area","line","part","item","unit","word",
    "gate","door","room","hall","yard","park","lake","tree","rock","road",
    "path","hill","farm","ship","boat","crew","port","zone","city","town",
    "site","shop","bank","mall","home","desk","seat","lamp","wire","pipe",
    "wall","roof","tile","belt","ring","tool","card","note","form","file",
    "data","info","page","user","name","like","tell","warn"
]

# -------------------------
#  GLOBALS
# -------------------------
display = None      # turtle for time & hint
score = 6
missed = []
right = []
inp_word = ""
word = choice(words)

# -------------------------
#  UPDATE RIGHT SIDE TEXT
# -------------------------
def update_display():
    display.clear()

    # Hint
    display.goto(180, 150)
    display.write(f"Hint: {choice(words)}", font=("Arial", 16, "bold"))

    # Time
    display.goto(180, 100)
    display.write(f"Time: {arrow.now().format('h:mm A')}", font=("Arial", 16, "normal"))
    t.update()
    t.ontimer(update_display, 1000)   # update every second


# -------------------------
#  MAIN GAME LOOP
# -------------------------
def start_game():
    global missed, right, inp_word, score

    scr = t.Screen()
    t.setup(600, 500)
    t.tracer(False)
    t.bgcolor("lavender")
    t.title("Guess the word game!")
    t.hideturtle()

    # Guess left text
    left = t.Turtle()
    left.up()
    left.hideturtle()
    left.goto(-270, 200)
    left.write(f"Guess left: {score}", font=("Arial", 16, "normal"))

    # Incorrect guesses label
    t.up()
    t.goto(-270, 150)
    t.write("Incorrect guesses:", font=("Arial", 16, "normal"))

    # Boxes for the 4-letter word
    for x in range(4):
        t.goto(-270 + 150 * x, -200)
        t.down()
        t.forward(95)
        t.up()

    # Circles (lives)
    circles = []
    for i in range(6):
        c = t.Turtle("circle")
        c.shapesize(3)
        c.color("black", "sky blue")
        c.up()
        c.goto(-150 + 50 * i, 0)
        circles.append(c)

    # Display turtle (time + hint)
    global display
    display = t.Turtle()
    display.hideturtle()
    display.up()

    # Start timed updates
    t.ontimer(update_display, 1000)

    # -------------------------
    #  INPUT LOOP
    # -------------------------
    while True:
        t.update()
        inp = input("Guess a letter: ").lower()

        if inp == "quit":
            sys.exit()

        # Correct guess
        if inp in word:
            inp_word += inp

            for i, letter in enumerate(word):
                if inp == letter:
                    t.goto(-270 + 150 * i, -200)
                    t.write(inp.upper(), font=("Arial", 48, "normal"))
                    right.append(inp)

            t.update()

            if len(right) == 4 and inp_word == word:
                messagebox.showinfo("End Game", "Great job! Correct word!")
                sys.exit()

        else:
            missed.append(inp)
            t.goto(-270 + 50 * len(missed), 150)
            t.write(inp.upper(), font=("Arial", 24, "normal"))

            score -= 1
            circles[-(6-score)].hideturtle()

            left.clear()
            left.goto(-270, 200)
            left.write(f"Guess left: {score}", font=("Arial", 16, "normal"))
            t.update()

            if score == 0:
                messagebox.showinfo("End Game", "You lost!")
                print(f"The word was: {word.upper()}")
                sys.exit()


# -------------------------
#  START GAME
# -------------------------
start_game()
