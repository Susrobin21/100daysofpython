from turtle import Turtle, Screen
import random
bet = False
screen = Screen()
screen.setup(600,600)
userbet = screen.textinput(title = 'Make a guess', prompt= 'Which turtle would win the race ? : ')
colors = ['red','yellow','orange','cyan','blue','purple','green']
y_index = [-120, -80, - 40, 0, 40, 80 , 120 ]
all_turtles = []
if userbet :
    bet = True


for start in range(0,7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[start])
    new_turtle.penup()
    new_turtle.goto(x = -280, y = y_index[start])
    all_turtles.append(new_turtle)


while bet :
    
    for turtle in all_turtles :
        if turtle.xcor() > 280 :
            winner = turtle.pencolor()
            if userbet == winner :
                print(f'You won the bet ! {winner} is winning color')
                quit()
            else :
                print(f'Blehhhh you lost , {winner} is the winning color')
                quit()
        dist = random.randint(0,10)
        turtle.forward(dist)







screen.exitonclick()