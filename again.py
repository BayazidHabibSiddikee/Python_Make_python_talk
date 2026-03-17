from PIL import Image , ImageDraw
import os, time, pyautogui
from turtle import *
from time import sleep
from tkinter import messagebox
import random
import sys

# ========================================
# 1. OPEN CAMERA → SCREENSHOT → CLOSE
# ========================================
os.system("start microsoft.windows.camera:")
time.sleep(2.3)

screenshot = pyautogui.screenshot()

time.sleep(0.5)
os.system("taskkill /IM WindowsCamera.exe /F")

# Convert screenshot to gray + RGB for turtle
scale = 0.25
dot_size = 2

img = screenshot.convert("L")
img = img.resize((int(img.width * scale), int(img.height * scale)))
img = img.convert("RGB")

# ========================================
# 2. START SCREEN + KEEP YOUR ANIMATION
# ========================================

screen = Screen()
colormode(255)
setup(int(img.width * dot_size)+50, int(img.height * dot_size)+50, 100, 50)

shape('turtle')
bgcolor('light yellow')
tracer(True)

c = Turtle('turtle')
c.shapesize(1)
c.color("black", "red")

colors = [
    (255, 182, 193), (173, 216, 230), (152, 251, 152),
    (230, 230, 250), (255, 218, 185), (255, 255, 224),
    (135, 206, 235), (240, 128, 128), (255, 253, 208),
    (200, 162, 200), (211, 211, 211), (245, 245, 220),
    (255, 255, 240), (255, 218, 185), (175, 238, 238),
    (176, 224, 230)
]

width, height = img.size
i = int(width * dot_size / 2)
j = int(height * dot_size / 2)

# ---------- YOUR ANIMATION (unchanged) ----------
for _ in range(1):
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
# -----------------------------------------------

# ========================================
# 3. DRAW THE SCREENSHOT FASTER
# ========================================

x_offset = -width * dot_size / 2
y_offset = height * dot_size / 2

bright_colors = ['white', 'light yellow']
dark_colors = ['black', 'darkblue']

t = Turtle()
t.hideturtle()
t.up()
t.speed(0)
tracer(False)
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        draw_x = x * dot_size + x_offset
        draw_y = y_offset - y * dot_size
        if r > 127:
            color = random.choice(bright_colors)
        else:
            color = random.choice(dark_colors)
        t.goto(draw_x, draw_y)
        t.dot(dot_size, color)
tracer(True)
update()
messagebox.showinfo("Done", "Drawing completed!")
done()
