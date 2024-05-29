from turtle import Turtle, Screen
import random
#shapes = ["triangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon"]
angles = [120 , 90 , 72 , 60 , 51.42857142857143 , 45 , 40 , 36]
turtle = Turtle()
sides = 3
turtle.pensize(5)
colors = ["red" , "blue" , "green" , "yellow" , "pink" , "purple" , "brown" , "cyan"]

for angle in angles:
    turtle.pencolor(random.choice(colors))
    for n in range(sides):
        turtle.right(angle)
        turtle.forward(100)

    sides += 1

screen = Screen()
screen.exitonclick()
