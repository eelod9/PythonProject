import turtle 
import random



t = turtle.Turtle()





turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

t.speed("fastest")
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        current_heading = t.heading()
        t.setheading(current_heading + size_of_gap)

draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()