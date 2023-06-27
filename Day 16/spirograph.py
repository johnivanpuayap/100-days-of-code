from turtle import Turtle, Screen
import random

def random_color():
    random_color = (random.choice(range(0, screen.colormode())), random.choice(range(0, screen.colormode())), random.choice(range(0, screen.colormode())))
    return random_color

def draw_spirograph(gap):
    angle = 0

    for i in range(360//gap):
        t.pencolor(random_color())
        t.setheading(t.heading() + gap)
        t.circle(100)


t = Turtle()
t.color("red")
t.speed('fastest')
screen = Screen()
screen.colormode(255)

draw_spirograph(5)

t.hideturtle()
screen.exitonclick()