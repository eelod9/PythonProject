from turtle import Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
tlist = []
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
#tlist.append(t1)
#tlist.append(t2)
#tlist.append(t3)


xcor = 0
for t in range(3):
    t = Turtle("square")
    t.color("white")
    t.goto(xcor,0)
    xcor -= 20
    tlist.append(t)




screen.exitonclick()