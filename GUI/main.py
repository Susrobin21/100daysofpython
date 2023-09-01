#from turtle import Turtle, Screen
#jimmy = Turtle()
#jimmy.showturtle()
#jimmy.color('red')
#my_screen = Screen()         # object = class()
#print(my_screen.canvheight)  # object.attribute
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon  name', ['pikachu', 'eevee','dialga'])
table.add_column('Type', ['electric','normal','dragon'])
table.align = 'l'
print(table)
