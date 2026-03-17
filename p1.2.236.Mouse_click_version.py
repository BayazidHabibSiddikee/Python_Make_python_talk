from turtle import *
from time import sleep
Screen()
setup(700,600,10,70)
hideturtle()
tracer(False)
pensize(5)
bgcolor('light yellow')
title("Connect four in turtle graphics")
for i in range(-250,350,100):
    up()
    goto(i,-350)
    down()
    goto(i,350)
    up()
pensize(1)
pencolor('grey')
for i in range(-200,300,100):
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()
#write column numbers
col = 1
#The red player moves first
turn = 'red'
#The x-cordinate of the center 7 columns
xs = [-300,-200,100,0,100,200,300]
#The y-cordinates of the center of 6 rows
ys = [-250,-150,-50,50,150,250]
#Keep track of occupied cells
occupied = [list() for _ in range(7)]
# create a second turtle module
fall = Turtle()
fall.up()
fall.hideturtle()


def conn(x,y):
    global turn
    if -350<x<350 and -350<y<350:
        col = int((x + 450)//100)
    else:
        print("You clicked outside the game board")
    row = len(occupied[col-1]) + 1
    # Show the disc fall from top
    if row<6:
        for i in range(6,row,-1):
            fall.goto(xs[col - 1],ys[i - 1])
            fall.dot(80,turn)
            update()
            sleep(0.08)
            fall.clear()
    up()
    goto(xs[col - 1],ys[row - 1])
    dot(80,turn)
    occupied[col - 1].append(turn)
    if turn == 'red':
        turn = 'yellow' 
    else:
        turn = 'red'
onscreenclick(conn)
listen()

for x in range(-300,350,100):
    goto(x,270)
    write(col,font=('Arial',20,'normal'))
    col+=1
done()
try:
    bye()
except:
    pass