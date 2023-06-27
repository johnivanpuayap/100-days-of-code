from turtle import Turtle, Screen
import random

def random_color():
    random_color = (random.choice(range(0, screen.colormode())), random.choice(range(0, screen.colormode())), random.choice(range(0, screen.colormode())))
    return random_color

t = Turtle()
t.color("red")
t.pensize(5)
t.speed('normal')
screen = Screen()
screen.colormode(255)

while True:
    t.pencolor(random_color())
    t.setheading(random.choice([0, 90, 180, 270]))
    t.forward(50)

t.hideturtle()
screen.exitonclick()