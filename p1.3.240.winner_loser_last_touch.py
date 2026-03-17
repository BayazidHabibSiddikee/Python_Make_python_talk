from turtle import *
from time import sleep
from tkinter import messagebox

Screen()
setup(700,600,10,70)
hideturtle()
tracer(False)
pensize(5)
bgcolor('light yellow')
title("Connect four in turtle graphics")

# Draw vertical lines
for i in range(-250,350,100):
    up()
    goto(i,-350)
    down()
    goto(i,350)
    up()

pensize(1)
pencolor('grey')

# Draw horizontal lines
for i in range(-200,300,100):
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()

# The red player moves first
turn = 'red'

# The x-coordinate of the center of 7 columns (FIXED: was [-300,-200,100,0,100,200,300])
xs = [-300,-200,-100,0,100,200,300]

# The y-coordinates of the center of 6 rows
ys = [-250,-150,-50,50,150,250]

# Keep track of occupied cells
occupied = [list() for _ in range(7)]

# Create a second turtle for animation
fall = Turtle()
fall.up()
fall.hideturtle()

# Create a list of valid inputs
validinputs = [1,2,3,4,5,6,7]

# Define horizontal function to check connect horizontally
def horizontal4(x,y,turn):
    win = False
    for dif in (-3,-2,-1,0):
        try:
            if occupied[x+dif][y] == turn \
            and occupied[x+dif+1][y]==turn\
            and occupied[x+dif+2][y] == turn \
            and occupied[x+dif+3][y]==turn\
            and x + dif>=0:
                win = True
        except IndexError:
            pass
    return win

# FIXED: renamed from vertical() to vertical4()
def vertical4(x,y,turn):
    win = False
    try:
        if occupied[x][y] == turn\
        and occupied[x][y-1]==turn\
        and occupied[x][y-2]==turn\
        and occupied[x][y-3]==turn\
        and y-3>=0:
            win = True
    except IndexError:
        pass
    return win

# Define forward4() function to check connecting 4 diagonally in / shape
def forward4(x, y, turn):
    win = False
    for dif in (-3, -2, -1, 0):
        try:
            if occupied[x+dif][y+dif] == turn\
            and occupied[x+dif+1][y+dif+1] == turn\
            and occupied[x+dif+2][y+dif+2] == turn\
            and occupied[x+dif+3][y+dif+3] == turn\
            and x+dif >= 0 and y+dif >= 0:
                win = True
        except IndexError:
            pass
    return win     

# Define back4() function to check connecting 4 diagonally in \ shape
def back4(x, y, turn):
    win = False
    for dif in (-3, -2, -1, 0):
        try:
            if occupied[x+dif][y-dif] == turn\
            and occupied[x+dif+1][y-dif-1] == turn\
            and occupied[x+dif+2][y-dif-2] == turn\
            and occupied[x+dif+3][y-dif-3] == turn\
            and x+dif >= 0 and y-dif-3 >= 0:
                win = True
        except IndexError:
            pass
    return win 

# Define win_game() function to check if someone wins the game
def win_game(col, row, turn):
    win = False
    # Convert column and row numbers to indexes in the list of lists occupied
    x = col-1
    y = row-1
    # Check all winning possibilities
    if vertical4(x, y, turn) == True:
        win = True
    if horizontal4(x, y, turn) == True:
        win = True
    if forward4(x, y, turn) == True:
        win = True
    if back4(x, y, turn) == True:
        win = True
    # Return the value stored in win
    return win

rounds = 1

def conn(x,y):
    global turn, rounds, validinputs
    
    if -350<x<350 and -350<y<350:
        # FIXED: column calculation was wrong (x + 450)
        col = int((x + 350)//100) + 1
    else:
        print("You clicked outside the game board")
        return  # FIXED: added return to exit function
    
    if col in validinputs:
        row = len(occupied[col-1]) + 1
        
        # Show the disc fall from top
        # FIXED: was row<6, should be row<=6 to handle all 6 rows
        if row <= 6:
            for i in range(6, row, -1):
                fall.goto(xs[col - 1], ys[i - 1])
                fall.dot(80, turn)
                update()
                sleep(0.08)
                fall.clear()
        
        # Place the disc
        up()
        goto(xs[col - 1], ys[row - 1])
        dot(80, turn)
        occupied[col - 1].append(turn)
        update()  # FIXED: added update() to display disc
        
        # Check if they won
        if win_game(col, row, turn) == True:
            validinputs = []
            messagebox.showinfo("End Game", f'Congrats player {turn}, you Won!!!')
        # If all cells are occupied and no winner, it's a tie
        elif rounds == 42:
            messagebox.showinfo("Tie Game", "Game over, it's a tie!")
        
        # Counting rounds
        rounds += 1
        
        # Update the list of valid moves
        if len(occupied[col-1]) == 6:
            validinputs.remove(col)
        
        # Switch turns
        if turn == 'red':
            turn = 'yellow' 
        else:
            turn = 'red'
    else:
        messagebox.showerror("Error", "Sorry, that's an invalid move!")

# FIXED: moved column number writing BEFORE onscreenclick()
col = 1
pencolor('black')
for x in range(-300, 350, 100):
    up()
    goto(x, 270)
    write(col, font=('Arial', 20, 'normal'))
    col += 1

update()  # FIXED: added update() to display numbers

onscreenclick(conn)
listen()

done()
try:
    bye()
except:
    pass