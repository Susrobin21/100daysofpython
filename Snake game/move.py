from turtle import Turtle, Screen
import time
MOVE_FORWARD = 20
STARTING_POSTIONS = [(0,0),(-20,0),(-40,0)]
parts = []
class Snake :
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.move()

    def create_snake(self):
        for position in STARTING_POSTIONS :
            new_part = Turtle(shape='square')
            new_part.penup()
            new_part.color('white')
            new_part.goto(position)
            self.parts.append(new_part)
    def move(self):
        for seg in range(len(self.parts)-1,0,-1):
            new_x = self.parts[seg - 1].xcor()
            new_y = self.parts[seg - 1].ycor()
            self.parts[seg].goto(new_x,new_y)
        self.parts[0].forward(MOVE_FORWARD)
        
    def up(self) :
        self.parts[0].setheading(90)
    
    def down(self):
        self.parts[0].setheading(270)

    def right(self):
        self.parts[0].setheading(0)

    def left(self):
        self.parts[0].setheading(180)
    

