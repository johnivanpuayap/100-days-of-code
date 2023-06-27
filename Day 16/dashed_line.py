from turtle import Turtle, Screen, window_width

t = Turtle()
t.color("red")
t.penup()
t.backward(370)

while t.xcor() < window_width() / 2 - 20:
    if t.isdown():
        t.penup()
    else:
        t.pendown()
    t.forward(10)

t.hideturtle()

screen = Screen()
screen.exitonclick()