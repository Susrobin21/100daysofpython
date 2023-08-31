#import colorgram
import turtle as Turtle
import random
#rgb = []
#colors = colorgram.extract('hirst.webp', 6)
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #colour = (r,g,b)
    #rgb.append(colour)

#print(rgb)   how to generate colors from a image

colorlist = [(227,226,225), (235, 236, 238), (231, 235, 232), (180, 6, 3), (2, 150, 7), (15, 25, 42), (150, 67, 129), (234,123,178), (20,234,123),(20,80,60),( 250, 9,7)]

Turtle.colormode(255)
kim = Turtle.Turtle()
kim.hideturtle()
kim.setheading(225)
kim.penup()
kim.forward(300)
kim.setheading(0)
number_of_dots = 100

for i in range(1,number_of_dots+1):
    kim.dot(20, random.choice(colorlist))
    kim.forward(50)
    if i %10 == 0 :
        kim.setheading(90)
        kim.forward(50)
        kim.setheading(180)
        kim.forward(500)
        kim.setheading(0)

screen = Turtle.Screen()
screen.exitonclick()