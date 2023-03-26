from turtle import Turtle, Screen
#etch sketch
timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.back(10)

def move_counterClockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def move_clockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def reset_turtle():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

timmy.pensize(5)
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=move_counterClockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=reset_turtle)



screen.exitonclick()