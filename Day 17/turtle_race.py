from turtle import Turtle, Screen
import random

def declare_winner(winner):
    if winner == user_bet:
        result = "You win"
    else:
        result = "You lose"
    
    print(f"{result}.The winner is the {winner} turtle!")

def start_race():
    while True:
        red.forward(random.randint(1, 20))
        green.forward(random.randint(1, 20))
        blue.forward(random.randint(1, 20))
        yellow.forward(random.randint(1, 20))
        orange.forward(random.randint(1, 20))
        violet.forward(random.randint(1, 20))

        if red.xcor() >= left_edge:
            declare_winner("red")
            break
        elif green.xcor() >= left_edge:
            declare_winner("green")
            break
        elif blue.xcor() >= left_edge:
            declare_winner("blue")
            break
        elif yellow.xcor() >= left_edge:
            declare_winner("yellow")
            break
        elif orange.xcor() >= left_edge:
            declare_winner("orange")
            break
        elif violet.xcor() >= left_edge:
            declare_winner("violet")
            break


screen = Screen()
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (ROYGBV): ").lower()

right_edge = screen.window_width()/-2 + 20
left_edge = screen.window_width()/2 - 50

red = Turtle()
red.shapesize(2, 2, 3)
red.shape("turtle")
red.color("red")
red.penup()
red.goto(right_edge, 125)

green = Turtle()
green.shapesize(2, 2, 3)
green.shape("turtle")
green.color("green")
green.penup()
green.goto(right_edge, 75)

blue = Turtle()
blue.shapesize(2, 2, 3)
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(right_edge, 25)

yellow = Turtle()
yellow.shapesize(2,2,3)
yellow.shape("turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(right_edge, -25)

orange = Turtle()
orange.shapesize(2,2,3)
orange.shape("turtle")
orange.color("orange")
orange.penup()
orange.goto(right_edge, -75)

violet = Turtle()
violet.shapesize(2,2,3)
violet.shape("turtle")
violet.color("violet")
violet.penup()
violet.goto(right_edge, -125)

start_race()

screen.exitonclick()
