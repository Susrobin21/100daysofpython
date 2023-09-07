from turtle import Turtle
from food import Food
from move import parts

food = Food()
turtle = Turtle()
class scoretrack(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,250)
        self.update()
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score : {self.score}", align='center', font=('arial',20,'normal'))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update()

        
        
        
        


        