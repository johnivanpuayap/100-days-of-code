from turtle import Turtle, Screen
from random import choice

colors = ["gray", "gold", "magenta", "teal", "navy", "silver", "olive", "indigo", "coral", "lavender"]

def draw_shape(number_sides):
    for i in range(1, number_sides + 1):
        
        t.forward(100)
        t.right(360/number_sides)
    
t = Turtle()
t.penup()
t.goto(-50, 150)
t.pendown()

for i in range(3, 11):
    t.pencolor(choice(colors))
    draw_shape(i)


t.hideturtle()

screen = Screen()
screen.exitonclick()