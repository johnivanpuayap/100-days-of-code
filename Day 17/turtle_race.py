from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

def declare_winner(winner):
    """Prints the result of the bet and the winner of the race. Accept a string parameter that will be declared as the winner"""
    if winner == user_bet:
        result = "YOU WIN!"
    else:
        result = "YOU LOSE!"
    
    print(f"{result} The winner is the {winner} turtle!")

def start_race(all_turtles):
    """Starts the race by moving the turtle to its starting position and moves the turtles"""
    
    y_position = 125
    for turtle in all_turtles:
        turtle.penup()
        turtle.goto(right_edge, y_position)
        y_position -= 50

    is_race_on = "True"

    while is_race_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() >= left_edge:
                declare_winner(turtle.pencolor())
                is_race_on = False

def ask_bet():
    """Asks the user on which turtle they want to bet on.
       Returns a string of the color they are betting."""
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color (ROYGBV): ")
    if user_bet is not None:
        return user_bet.lower()
    else:
        return None
    
def create_turtles():
    """Generates the turtles for the race.
       Returns a list of turtles.
    """
    
    turtles = []

    for i in range(0, 6):
        t = Turtle()
        t.shapesize(2, 2, 3)
        t.shape("turtle")
        t.color(colors[i])
        turtles.append(t)
    
    return turtles

screen = Screen()
screen.title("Betting Turtle Race")

user_bet = ""

while user_bet not in colors:
    user_bet = ask_bet()

right_edge = screen.window_width()/-2 + 20
left_edge = screen.window_width()/2 - 50

all_turtles = create_turtles()
start_race(all_turtles)

screen.exitonclick()
