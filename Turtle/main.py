from turtle import Turtle, Screen

import random
import turtle as t

t.colormode(255)


timmy = t
timmy.shape("turtle")
timmy.color("#FFB6C1")
def dashed_line():
    for _ in range(4):
        timmy.penup()
        timmy.forward(25)
        timmy.pendown()
        timmy.forward(25)
    
"""
for _ in range(4):
    timmy.right(90)
    dashed_line()
"""



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


def multiplePolygons(edges):
    angle = 360 /edges
    random_color  = random_color()
    timmy.pencolor(random_color)
    timmy.pensize(10)
    for _ in range(edges):
        timmy.right(angle)
        timmy.forward(100)


#for i in range(3,11):
 #   multiplePolygons(i)
directions =[0, 90, 180, 270]
timmy.speed("fast")
while True:
    timmy.pencolor(random_color())
    timmy.pensize(10)
    pos = random.choice(directions)
    timmy.setheading(pos)
    timmy.forward(30)
    

   
    


















screen = Screen()
screen.exitonclick()