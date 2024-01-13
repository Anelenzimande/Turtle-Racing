from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.title("blue, red, yellow, green, cyan, orange")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a colour: ").lower()
colors = ["blue", "red", "yellow", "green", "cyan", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
               result = print(f"You've Won! with the {winning_color} turtle")


            else:
                result = print(f"You've Lost! , the {winning_color} turtle was the victor!")


        turtle_speed = random.randint(0, 10)
        turtle.forward(turtle_speed)




screen.exitonclick()