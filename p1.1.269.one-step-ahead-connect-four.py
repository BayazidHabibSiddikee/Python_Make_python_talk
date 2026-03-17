from turtle import *
from time import sleep
from tkinter import messagebox
from random import choice
from copy import deepcopy
import sys

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

# The x-coordinate of the center of 7 columns
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
def horizontal4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3,-2,-1,0):
        try:
            if board[x+dif][y] == color \
            and board[x+dif+1][y] == color\
            and board[x+dif+2][y] == color \
            and board[x+dif+3][y] == color\
            and x + dif >= 0:
                win = True
        except IndexError:
            pass
    return win

# Define vertical4() function
def vertical4(x, y, color, board):  # FIXED: added board parameter
    win = False
    try:
        if board[x][y] == color\
        and board[x][y-1] == color\
        and board[x][y-2] == color\
        and board[x][y-3] == color\
        and y-3 >= 0:
            win = True
    except IndexError:
        pass
    return win

# Define forward4() function to check connecting 4 diagonally in / shape
def forward4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3, -2, -1, 0):
        try:
            if board[x+dif][y+dif] == color\
            and board[x+dif+1][y+dif+1] == color\
            and board[x+dif+2][y+dif+2] == color\
            and board[x+dif+3][y+dif+3] == color\
            and x+dif >= 0 and y+dif >= 0:
                win = True
        except IndexError:
            pass
    return win     

# Define back4() function to check connecting 4 diagonally in \ shape
def back4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3, -2, -1, 0):
        try:
            if board[x+dif][y-dif] == color\
            and board[x+dif+1][y-dif-1] == color\
            and board[x+dif+2][y-dif-2] == color\
            and board[x+dif+3][y-dif-3] == color\
            and x+dif >= 0 and y-dif-3 >= 0:
                win = True
        except IndexError:
            pass
    return win 

# Define win_game() function to check if someone wins the game
def win_game(col, row, color, board):  # FIXED: added board parameter
    win = False
    # Convert column and row numbers to indexes
    x = col-1
    y = row-1
    # Check all winning possibilities
    if vertical4(x, y, color, board) == True:
        win = True
    if horizontal4(x, y, color, board) == True:
        win = True
    if forward4(x, y, color, board) == True:
        win = True
    if back4(x, y, color, board) == True:
        win = True
    return win

rounds = 1

# Define computer AI function
def computer_best_move():
    global occupied, validinputs, turn
    
    # Try to win
    for move in validinputs:
        test = deepcopy(occupied)
        test[move-1].append(turn)
        row = len(test[move-1])
        if win_game(move, row, turn, test):
            return move
    
    # Try to block opponent
    opponent = 'yellow' if turn == 'red' else 'red'
    for move in validinputs:
        test = deepcopy(occupied)
        test[move-1].append(opponent)
        row = len(test[move-1])
        if win_game(move, row, opponent, test):
            return move
    
    # Default: center or random
    return 4 if 4 in validinputs else choice(validinputs)

# Function to execute a move
def make_move(col, is_computer=False):
    global turn, rounds, validinputs
    
    if col not in validinputs:
        return False
    
    row = len(occupied[col-1]) + 1
    
    # Show the disc fall from top
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
    update()
    
    # Check if won
    if win_game(col, row, turn, occupied) == True:
        validinputs = []
        player_name = "Computer" if is_computer else "Player"
        messagebox.showinfo("End Game", f'Congrats {player_name} ({turn}), you Won!!!')
        return True
    
    # Check for tie
    if rounds == 42:
        messagebox.showinfo("Tie Game", "Game over, it's a tie!")
        return True
    
    # Update game state
    rounds += 1
    if len(occupied[col-1]) == 6:
        validinputs.remove(col)
    
    # Switch turns
    if turn == 'red':
        turn = 'yellow' 
    else:
        turn = 'red'
    
    return False

# Player click handler
def conn(x, y):
    global turn, validinputs
    
    if -350 < x < 350 and -350 < y < 350:
        col = int((x + 350)//100) + 1
    else:
        print("You clicked outside the game board")
        return
    
    if col not in validinputs:
        messagebox.showerror("Error", "Sorry, that's an invalid move!")
        return
    
    # Player makes move
    game_over = make_move(col, is_computer=False)
    
    if game_over or len(validinputs) == 0:
        return
    
    # Computer makes move
    sleep(0.5)
    col = computer_best_move()
    make_move(col, is_computer=True)

# Write column numbers
col = 1
pencolor('black')
for x in range(-300, 350, 100):
    up()
    goto(x, 270)
    write(col, font=('Arial', 20, 'normal'))
    col += 1

update()

onscreenclick(conn)
listen()

done()
try:
    bye()
except:
    pass