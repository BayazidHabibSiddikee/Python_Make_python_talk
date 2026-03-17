import time, threading, random, sys, arrow, turtle as t 
from tkinter import messagebox

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

#x.tracer(False)
t.Screen().bgcolor("lavender")
t.setup(600, 500)
t.hideturtle()
t.tracer(False)
#t.title("Guess the Word Game")
t.up()
x = t.Turtle()
x.hideturtle()
x.up()

def title_screen():
    #try:
    while True:
        #t.clear()
        t.title(f"Guess the Word Game   |   {arrow.now().format('h:mm A')}  |  Hint1: {random.choice(words)}    |   Hint2: {random.choice(words)}")
        time.sleep(1)
        #t.update()
        #t.ontimer(title_screen, 1000)
#    except:
#       t.title("Guess the Word Game")

def main():
    t.goto(-270,200)
    t.write("Welcome to the Guess the Word Game!", font=("Arial", 20, "bold"))
    t.update()
    time.sleep(2)
    t.clear()
    t.goto(-270,200)
    t.write("Try to guess the 4-letter word!", font=("Arial", 16, "normal"))
    t.update()
    time.sleep(2)
    t.clear()
    t.goto(-270,200)
    t.write("You have 6 attempts. Good luck!", font=("Arial", 16, "normal"))
    t.update()
    time.sleep(2)
    t.clear()
    score = 6
    t.goto(-270,200)
    t.write(f"Attempts left: {score}", font=("Arial", 16, "normal"))
    t.up()
    t.goto(-270,150)
    t.write("Incorrect guesses:", font=("Arial", 16, "normal"))
    t.up()
    word = random.choice(words)
    for i in range(len(word)):
        x.goto(-270 + 150 * i, -200)
        x.pendown()
        x.forward(100)
        x.penup()
    t.update()

    circles = []
    for i in range(6):
        c = t.Turtle("circle")
        c.shapesize(3)
        c.color("black", "sky blue")
        c.up()
        c.goto(-150 + 50 * i, 0)
        circles.append(c)
        #time.sleep(1)
    t.update()
    #time.sleep(2)
    
    missed = []
    right = []
    while True:
        inp_word = t.textinput("Guess the Word", "Enter a letter:").lower()
        if inp_word is None or len(inp_word) != 1 or not inp_word.isalpha():
            messagebox.showwarning("Warning", "Please enter a single letter.")
            continue
        if inp_word in missed or inp_word in right:
            messagebox.showwarning("Already Guessed", "You already guessed that letter!")
            continue
        if inp_word in word:
            right.append(inp_word)
            for i in range(len(word)):
                if word[i] == inp_word:
                    x.goto(-270 + 150 * i ,-200)
                    x.write(inp_word.upper(), font=("Arial", 48, "bold"))
            t.update()
            if all(letter in right for letter in word):
                messagebox.showinfo("Congratulations!", f"You guessed the word '{word.upper()}' correctly!")
                sys.exit()
        else:
            missed.append(inp_word)
            score -=1
            t.goto(-270, 150)
            t.clear()
            t.write("Incorrect guesses: " + ", ".join(missed), font=("Arial", 16, "normal"))
            t.update()
            t.goto(-270, 200)
            circles[-(6-score)].hideturtle()
            #t.clear()
            t.write(f"Attempts left: {score}", font=("Arial", 16, "normal"))
            t.update()
            if score == 0:
                messagebox.showinfo("Game Over", f"You've run out of attempts! The word was '{word.upper()}'.")
                sys.exit()  
    mainloop()

if __name__ == "__main__":
    #threading.Thread(target=title_screen,args=(),daemon=True).start()
    #threading.Thread(target=main,args=(),daemon=True).start()
    main()
    t.done()
    try:
        t.bye()
    except:
        pass