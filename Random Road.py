from turtle import Turtle, Screen
import random
beast = Turtle()
beast.pensize(5)
beast.speed(0)
colors = ["red" , "blue" , "green" , "yellow" , "pink" , "purple" , "brown" , "cyan"]
steps = int(input("How many steps shoud he make?"))

def going():
    beast.pencolor(random.choice(colors))
    turns = random.randint(1,4)
    for _ in range(turns):
        beast.right(90)
    beast.forward(30)

for _ in range(steps):
    going()


screen = Screen()
screen.exitonclick()