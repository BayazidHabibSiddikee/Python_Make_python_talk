from turtle import *
from time import sleep
from tkinter import messagebox
import random
import sys, os
from PIL import Image

# --- 1. Image Processing Settings (PIL) ---
# IMPORTANT: Change the path to your actual image file location
try:
    #path = r"E:\YT\images\john.png"
    path = textinput("Enter the image file path", "Enter Path:")
    if os.path.exists(path) == False:
        raise FileNotFoundError
except:
    path = r"E:\YT\images\remove-photos-background-removed.png"

scale = 1      # Scale down the image (0.5 means 1/2 size - faster!)
dot_size = 2     # Size of the dot (pixel) on the Turtle canvas

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
    
screen = Screen()
colormode(255)
setup(int(img.width * dot_size), int(img.height * dot_size), 100, 50)
i = int(img.width * dot_size / 2)
j = int(img.height * dot_size / 2)

shape('turtle')
bgcolor('light yellow')
tracer(True)

c = Turtle('turtle')
c.shapesize(1)
c.color("black", "red")

colors = [
        (255, 182, 193),   # Light pink
        (173, 216, 230),   # Baby blue
        (152, 251, 152),   # Mint green
        (230, 230, 250),   # Lavender
        (255, 218, 185),   # Peach
        (255, 255, 224),   # Pale yellow
        (135, 206, 235),   # Sky blue
        (240, 128, 128),   # Light coral
        (255, 253, 208),   # Cream
        (200, 162, 200),   # Lilac
        (211, 211, 211),   # Light gray
        (245, 245, 220),   # Beige
        (255, 255, 240),   # Ivory
        (255, 218, 185),   # Pastel peach
        (175, 238, 238),   # Soft aqua
        (176, 224, 230),    # Powder blue
    ]
for _ in range(15):
    for k in range(-i, i, 20):
        c.shape(random.choice(['turtle','circle','arrow','square','triangle','classic']))
        shape(random.choice(['turtle','circle','arrow','square','triangle','classic']))
        speed(0.0001)
        color("black", random.choice(colors))
        c.speed(0.0001)
        c.color("black", random.choice(colors))
        c.goto(k, random.randint(-j, j))
        pensize(random.randint(1, 4))
        pencolor(random.choice(colors))
        goto(k, random.randint(-j, j))
        sleep(0.005)
        c.color("black", random.choice(colors))
        dot(10)
        
    c.goto(100, 0)
    sleep(0.5)

c.hideturtle()
hideturtle()

#messagebox.showinfo("Info", "Let's the real drawing begin... Please wait.")

try:
    # Resize the image based on the scale factor
    img = img.resize((int(img.width * scale), int(img.height * scale)))
    # Calculate the offsets needed to center the drawing on the Turtle canvas (0, 0)
    x_offset = -img.width / 2
    y_offset = img.height / 2

    colormode(255) 
    tracer(False)  # FIXED: Turn OFF tracer BEFORE creating turtle for speed!
    
    t = Turtle()
    t.up()  # Keep the pen up when moving
    t.speed(0)  # FIXED: Set turtle speed to 0 (fastest)
    #tracer(True)  # Turn off screen updates for faster drawing
    # Loop through every pixel in the (scaled) image
    #speed(0.0001)
    #t.speed(0.0001)
    bright_colors = ['white', 'yellow','light yellow']
    dark_colors = ['black', 'darkblue', 'purple']
    
    # Loop through every pixel in the (scaled) image
    for y in range(img.height):
        for x in range(img.width):
            # 1. Get the RGB color tuple (r, g, b)
            # Since the image is grayscale, r == g == b
            r, g, b = img.getpixel((x, y))
            
            # 2. Convert to Turtle Drawing Coordinates (Center origin, Y-axis flipped)
            draw_x = (x + x_offset) * dot_size
            draw_y = (y_offset - y) * dot_size

            # 3. Draw the colored dot - bright colors for white, dark for black
            # FIXED: Use brightness to choose color
            brightness = r  # Since grayscale, r == g == b
            if brightness > 127:  # White areas
                color = random.choice(bright_colors)
            else:  # Black areas
                color = random.choice(dark_colors)
            
            t.goto(draw_x, draw_y)
            t.dot(dot_size, color)
    t.hideturtle()
    tracer(True)  # Turn screen updates back on to show the final result
    update()  # FIXED: Force update to display the image
    messagebox.showinfo("Info", "Black and white image drawing complete!")
    
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {str(e)}")
    sys.exit()

done()
try:
    bye()
except:
    pass