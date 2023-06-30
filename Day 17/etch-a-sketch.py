from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_right():
    t.right(10)

def turn_left():
    t.left(10)

def clear_drawing():
    t.clear()
    t.home()
    
screen.listen()
screen.onkey(move_forward, "W")
screen.onkey(move_forward, "w")

screen.onkey(move_backward, "S")
screen.onkey(move_backward, "s")

screen.onkey(turn_left, "A")
screen.onkey(turn_left, "a")

screen.onkey(turn_right, "D")
screen.onkey(turn_right, "d")

screen.onkey(key="C", fun=clear_drawing)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()