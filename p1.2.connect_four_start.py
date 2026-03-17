from turtle import *
from time import sleep
from tkinter import messagebox
import random
from copy import deepcopy
import sys

Screen()
setup(700,700,100,50)
#hideturtle()
tracer(False)
shape('turtle')
pensize(5)
'''
dot(10,'red')
forward(200)
dot(10,'yellow')
right(90)
up()
backward(100)
dot(100,'blue')
goto(0,0)
dot(50,'green')'''
'''
pencolor('blue')
for i in range(-350,350,10):
    pensize(1)
    up()
    goto(i,-350)
    #dot(5,'blue')
    down()
    goto(i,350)
    up()
pencolor('brown')
for i in range(-350,350,10):
    pensize(1)
    up()
    goto(-350,i)
    #dot(5,'blue')
    down()
    goto(350,i)
'''
bgcolor('light yellow')
tracer(True)
'''
for i in [350,350,-350,-350]:
    goto(i,0)
    dot(50,'red')
    goto(0,i)
    dot(50,'red')
    goto(i,i)
    dot(50,'red')
    goto(i,-i)
    dot(50,'red')
    goto(-i,i)
    dot(50,'red')
    goto(-i,-i)
    dot(50,'red')
    goto(0,i)
'''


c = Turtle('circle')
c.shapesize(2)              # make it bigger
c.color("black", "red")  # black outline, yellow fill
#c.up()
tracer(True)
for j in range(15):
    for i in range(-300,300,20):
        c.goto(i,random.randint(-350,350))
        pensize(random.randint(1,4))
        pencolor(random.choice(['red','yellow','blue','green','orange','purple']))

        goto(random.randint(-300,300),i)
        sleep(0.05)
        c.color("black", random.choice(['red','yellow','blue','green','orange','purple']))
        dot(10)
        
    c.goto(100,0)
    sleep(0.5)
c.hideturtle()


'''# Draw the image using Turtle graphics'''
'''
from PIL import Image
import sys

# --- 1. Image Processing Settings (PIL) ---
# IMPORTANT: You must change the path below to the actual location of your image file.
# Example: path = 'C:/Users/YourName/Desktop/my_image.jpg' 
path = '/home/sword/Pictures/lisa.png' 
scale = 0.5      # Scale down the image (0.25 means 1/4 size, drawing 1/16 the pixels)
dot_size = 2      # Size of the dot (pixel) on the Turtle canvas

# Open, convert, and resize the image
try:
    # 1. Open the image
    img = Image.open(path)
    # 2. Convert to Grayscale ('L' mode - Luminosity)
    img = img.convert("L") 
    # 3. Convert back to RGB for Turtle drawing (R=G=B for grayscale)
    img = img.convert("RGB") 
except FileNotFoundError:
    print(f"Error: Image file not found at {path}. Please check the path and file name.")
    sys.exit()

# Resize the image based on the scale factor
img = img.resize((int(img.width * scale), int(img.height * scale)))

# Calculate the offsets needed to center the drawing on the Turtle canvas (0, 0)
x_offset = -img.width / 2
y_offset = img.height / 2

colormode(255) 
t = Turtle()
t.hideturtle()
t.up() # Keep the pen up when moving
# Loop through every pixel in the (scaled) image
for y in range(img.height):
    for x in range(img.width):
        
        # 1. Get the RGB color tuple (r, g, b)
        # Since the image is grayscale, r == g == b
        r, g, b = img.getpixel((x, y))

        # 2. Convert to Turtle Drawing Coordinates (Center origin, Y-axis flipped)
        draw_x = (x + x_offset) * dot_size
        draw_y = (y_offset - y) * dot_size

        # 3. Draw the colored dot
        t.color(r, g, b)
        t.goto(draw_x, draw_y)
        t.dot(dot_size)

tracer(True) # Turn screen updates back on to show the final result
print("Black and white image drawing complete!")'''

done()
try:
    bye()
except:
    pass