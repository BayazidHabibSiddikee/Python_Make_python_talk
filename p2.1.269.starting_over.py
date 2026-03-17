from turtle import *
from time import sleep
from tkinter import messagebox
from random import choice
from copy import deepcopy
import sys


Screen()
setup(700,600,10,70)
hideturtle()
shape('turtle')
pensize(5)
bgcolor('light yellow')
title("Connect four in turtle graphics")

#Let's build the board
# Draw vertical lines
tracer(False)
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
    
turn = 'red'  # The red player moves first
'''Center x-coordinates of 7 columns'''
xs = [-300,-200,-100,0,100,200,300]
'''Center y-coordinates of 6 rows'''
ys = [-250,-150,-50,50,150,250]
'''Keep track of occupied cells'''

occupied = [list() for _ in range(7)]

#Create animation turtle
fall = Turtle('circle')
fall.up()
fall.hideturtle()
#Create a list of valid inputs
validinputs = [a for a in range(1,8)]
rounds = 1


#Define horizontal function to check connect horizontally
def horizontal4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3,-2,-1,0):
        try:
            if board[x + dif][y]==color\
            and board[x + dif + 1][y]==color\
            and board[x + dif + 2][y]==color\
            and board[x + dif + 3][y]==color \
            and x + dif >= 0:
                win = True
        except IndexError:
            pass
    return win

#Define vertical function to check connect vertically
def vertical4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3,-2,-1,0):
        try:
            if board[x][y + dif]==color\
            and board[x][y + dif + 1]==color\
            and board[x][y + dif + 2]==color\
            and board[x][y + dif + 3]==color \
            and y + dif >= 0:
                win = True     
        except IndexError:
            pass
    return win 

#Define diagonal function to check connect diagonally
def diagonal4(x, y, color, board):  # FIXED: added board parameter
    win = False
    for dif in (-3,-2,-1,0):
        try:
            if board[x + dif][y + dif]==color\
            and board[x + dif + 1][y + dif + 1]==color\
            and board[x + dif + 2][y + dif + 2]==color\
            and board[x + dif + 3][y + dif + 3]==color\
                and x + dif >= 0 and y + dif >= 0:
                    win = True
        except IndexError:
            pass
    for dif in (-3,-2,-1,0):
        try:
            if board[x + dif][y - dif]==color\
            and board[x + dif + 1][y - dif - 1]==color\
            and board[x + dif + 2][y - dif - 2]==color\
            and board[x + dif + 3][y - dif - 3]==color\
                and x + dif >= 0 and y - dif <= 5:
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

def win_game(col, row, color, board):  # FIXED: added board parameter
    win = False
    x = col -1
    y = row -1
    if horizontal4(x, y, color, board) == True:
        win = True
    if vertical4(x, y, color, board) == True:
        win = True
    if forward4(x, y, color, board) == True:
        win = True
    if back4(x, y, color, board) == True:
        win = True
    if diagonal4(x, y, color, board) == True:
        win = True
    return win

def computer_best_move():
    global occupied, turn, validinputs
    for move in validinputs:
        test = deepcopy(occupied)
        test[move - 1].append(turn)
        row = len(test[move - 1])
        if win_game(move, row, turn, test):
            return move
    # try to block opponent's win
    opponent = 'yellow' if turn == 'red' else 'red'
    for move in validinputs:
        test = deepcopy(occupied)
        test[move - 1].append(opponent)
        row = len(test[move - 1])
        if win_game(move, row, opponent, test):
            return move
    # otherwise, choose random move
    return choice(validinputs)

def make_move(col, is_computer=False):
    global turn, occupied, validinputs, rounds
    if col not in validinputs:
        return False
    row = len(occupied[col - 1]) + 1
    # Animate the falling piece
    if row<=6:
        for i in range(6, row, -1):
            fall.goto(xs[col - 1],ys[i - 1])
            fall.dot(80, turn)
            update()
            sleep(0.1)
            fall.clear()
    # Place the piece
    up()
    goto(xs[col - 1], ys[row - 1])
    dot(80, turn)
    occupied[col - 1].append(turn)
    update()
    # Check for win
    if win_game(col, row, turn, occupied):
        validinputs.clear()
        player_name = "Computer" if is_computer else "Player"
        messagebox.showinfo("Game Over", f"{player_name} ({turn}) wins!")
        sys.exit()
        #return True
    # Check for draw
    if rounds == 42:
        messagebox.showinfo("Game Over", "It's a draw!")
        sys.exit()
#        return True
    # Switch turns
    rounds += 1
    turn = 'yellow' if turn == 'red' else 'red'
    return False


def conn(x,y):
    global turn, validinputs, rounds
    
    if -350 < x < 350 and -300<y<350:
        col = int((x + 350)//100 + 1)
    else:
        messagebox.showinfo("Invalid Move", "Click inside the board to make a move.")
        return
    
    if col not in validinputs:
        messagebox.showinfo("Invalid Move", "Column full! Choose another column.")
        return
    
    game_over = make_move(col,is_computer=False)
    
    if game_over or len(validinputs) == 0:
        return
    # Computer's turn
    sleep(0.5)
    col = computer_best_move()
    make_move(col,is_computer=True)
    
# write col number 
col = 1
pencolor('black')
for x in range(-300, 350, 100):
    up()
    goto(x, 270)
    write(col, align='center', font=('Arial', 20, 'bold'))
    col += 1

update()
onscreenclick(conn)
listen()
done()
try:
    bye()
except:
    pass