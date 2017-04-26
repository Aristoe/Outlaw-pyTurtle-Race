# Outlaw-pyTurtle-Race
# Turtle Race in Python 2.7

import turtle
import random
wn = turtle.Screen()
wn.bgcolor('lightgrey')

filler = turtle.Turtle()
filler.color('white')
filler.up()
filler.goto(225,125)
filler.down()
filler.begin_fill()
filler.goto(225,-75)
filler.goto(-325,-75)
filler.goto(-325,125)
filler.goto(225,125)
filler.end_fill()

waylon = turtle.Turtle()    #define 4 turtles and finish
willie = turtle.Turtle()
bonnie = turtle.Turtle()
clyde = turtle.Turtle()
finish = turtle.Turtle()
waylon.color('red')         #define color
willie.color('green')
bonnie.color('purple')
clyde.color('blue')
finish.color('black')

waylon.up()                 #STARTING POSITIONS!
waylon.goto(-300, 100)
waylon.down()
willie.up()
willie.goto(-300, 50)
willie.down()
bonnie.up()
bonnie.goto(-300, 0)
bonnie.down()
clyde.up()
clyde.goto(-300, -50)
clyde.down()

finish.up()                 #Get Set!
finish.goto(200,125)
finish.down()
finish.right(90)
finish.forward(201)
finish.up()
finish.goto(233,25)
finish.right(90)

for i in range(1000):         # GO!
    waylon.forward(random.random())
    willie.forward(random.random())
    bonnie.forward(random.random())
    clyde.forward(random.random())


wn.exitonclick()            #keep window open until manually closed
