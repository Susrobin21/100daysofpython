from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height= 800, width= 800)
screen.bgcolor('black')
screen.title('Snek game ')
screen.tracer(0)
starting_positions = [(0,0),(-20,0),(-40,0)]
parts = []

for position in starting_positions :
    new_part = Turtle(shape='square')
    new_part.penup()
    new_part.color('white')
    new_part.goto(position)
    parts.append(new_part)

game = True
while game :
    screen.update()
    time.sleep(0.1)
    for seg in range(len(parts)-1,0, 1) :
        new_x = parts[seg - 1].xcor()
        new_y = parts[seg - 1].ycor()
        (parts[seg]).goto(new_x,new_y)
   
        
    
    









screen.exitonclick()