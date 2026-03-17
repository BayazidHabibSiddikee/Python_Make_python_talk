'''   1  2   3   4   5   6   7
    ┌───┬───┬───┬───┬───┬───┬───┐
    │   │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │   │
    ├───┼───┼───┼───┼───┼───┼───┤
    │   │   │   │   │   │   │   │
    └───┴───┴───┴───┴───┴───┴───┘
'''

from turtle import *
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
for x in range(-300,350,100):
    goto(x,270)
    write(col,font=('Arial',20,'normal'))
    col+=1
done()
try:
    bye()
except:
    pass