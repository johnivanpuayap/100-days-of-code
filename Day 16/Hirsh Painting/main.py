###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('Day 16\\Hirsh Painting\\image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

def random_color():
    """Returns a random color from a list of colors generated by colorgram"""
    random_color = random.choice(rgb_colors)
    return random_color

t = Turtle()
t.color("red")
t.speed('fastest')
t.hideturtle()
screen = Screen()
screen.colormode(255)

# set the turte to the top left
t.penup()
t.goto(-350, 280)

while t.ycor() > -280:
    while t.xcor() <= 350:
        t.pendown()
        t.dot(25, random_color())
        t.penup()
        t.goto(t.xcor() + 50, t.ycor())
    t.goto(-350, t.ycor() - 50)

screen.exitonclick()