from turtle import Turtle,Screen
import random

timmy = Turtle()
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
color_list = ["#FF0000","#98FB98","#00FFFF","#EE82EE", "#9400D3", "#FFA500", "#87CEFA"]
def multiplePolygons(edges):
    angle = 360 /edges
    random_color  = random.choice(color_list)
    timmy.pencolor(random_color)
    timmy.pensize(10)
    for _ in range(edges):
        timmy.right(angle)
        timmy.forward(100)


for i in range(3,11):
    multiplePolygons(i)


   
    


















screen = Screen()
screen.exitonclick()