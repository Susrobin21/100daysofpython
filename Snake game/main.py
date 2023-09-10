from turtle import Turtle, Screen
import time
from move import Snake
from food import Food
from scoreboard import scoretrack
screen = Screen()
screen.setup(height= 600, width= 600)
screen.bgcolor('black')
screen.title('Snek game ')
screen.tracer(0)
snake = Snake()
food = Food()
scoree = scoretrack()
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
    if snake.parts[0].distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoree.increase_score()
    if snake.parts[0].xcor() > 280 or snake.parts[0].xcor() < -280 or snake.parts[0].ycor() > 280 or snake.parts[0].ycor() < -280 :
        game = False
        scoree.game_over()
    for segment in snake.parts:
        if segment == snake.parts9[0]:
            pass
        if snake.parts[0].distance(segment) < 10:
            game = False
            scoree.game_over()

        
    
    








screen.exitonclick()
