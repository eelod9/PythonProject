from turtle import Turtle, Screen
import random
screen = Screen()
#screen.setup(width = 500, height = 400)

user_answer = screen.textinput("Make your bet!", "Who will win the race? Enter a colour:")
screen.colormode(255)

color_list = [ "red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
start_Position = -200

for i, value in enumerate(color_list):
    k = Turtle()    
    k.color(value)
    k.penup()
    start_Position+= 50
    k.setposition(-400,start_Position)
    k.shape("turtle")
    k.shapesize(2)
    turtle_list.append(k)

is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 400:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_answer:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")
            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


    










screen.exitonclick()