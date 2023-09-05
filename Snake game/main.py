from turtle import Turtle, Screen
import time
from move import Snake
screen = Screen()
screen.setup(height= 800, width= 800)
screen.bgcolor('black')
screen.title('Snek game ')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game = True
while game :
    screen.update()
    time.sleep(0.1)
    snake.move()
        
    
    








screen.exitonclick()