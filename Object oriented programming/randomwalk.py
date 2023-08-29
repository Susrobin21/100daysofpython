from turtle import Turtle, Screen
import random

slippin_jimmy = Turtle()
Turtle.colormode(255)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_colors

directions = [0, 90, 180, 270]
slippin_jimmy.pensize(15)
slippin_jimmy.shape('circle')
slippin_jimmy.speed('fastest')


for i in range(200):
    slippin_jimmy.color(random_colors())
    slippin_jimmy.forward(50)
    slippin_jimmy.setheading(random.choice(directions))
