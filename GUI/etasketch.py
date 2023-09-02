from turtle import Turtle,Screen

kimmy = Turtle()

screen = Screen()

def forward():
    
    kimmy.forward(10)

def backward():
    kimmy.back(10)

def right():
    new = kimmy.heading() + 10 
    kimmy.setheading(new)

def left():
    new = kimmy.heading() - 10 
    kimmy.setheading(new)

def clear():
    kimmy.clear()
    kimmy.penup()
    kimmy.home()
    kimmy.pendown()

screen.listen()
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(right, 'd')
screen.onkey(left, 'a')
screen.onkey(clear, 'c')

screen.exitonclick()