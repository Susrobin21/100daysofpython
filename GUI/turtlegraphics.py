from turtle import Turtle, Screen
import random
jimmy = Turtle()
jimmy.shape('turtle')

jimmy.speed('fast')
def circle():
    for i in range(0,361):
        jimmy.forward(1)
        jimmy.right(1)
#circle()

def square():
    for i in range(0,4):
        jimmy.forward(100)
        jimmy.right(90)
#square() to create square

def dashed_line():
    for i in range(0,10):
        jimmy.pendown()
        jimmy.forward(10)
        jimmy.penup()
        jimmy.forward(10)
#dashed_line()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def all_shapes():
    for j in range (4,10):
        for i in range(0,j):
            jimmy.forward(100)
            jimmy.right(360/j)       

for shape_side_n in range(3, 10):
    jimmy.color(random.choice(colours))
all_shapes()

my_screen = Screen()
my_screen.exitonclick()