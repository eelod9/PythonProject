from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
STARTING_POSITIONS_LEFT = (-350,0)
STARTING_POSITIONS_RIGHT = (350,0)



screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
the_Ball = Ball()
r_Paddle = Paddle(STARTING_POSITIONS_RIGHT)
l_Paddle = Paddle(STARTING_POSITIONS_LEFT)
board = Scoreboard()
screen.listen()
screen.onkey(r_Paddle.go_up,"Up")
screen.onkey(r_Paddle.go_down,"Down")
screen.onkey(l_Paddle.go_up,"w")
screen.onkey(l_Paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(the_Ball.move_speed)
    screen.update()
    the_Ball.move()
    #Detect collision with wall
    if (the_Ball.ycor() > 280 or the_Ball.ycor() < -280):
        the_Ball.bounce_y()
    #Detect collision with both paddle
    if the_Ball.distance(r_Paddle) < 50 and the_Ball.xcor() > 320 or the_Ball.distance(l_Paddle) <50 and the_Ball.xcor() <-320:
        the_Ball.bounce_x()
        
        

    #Detect R paddle miss
    if the_Ball.xcor() > 380:
        the_Ball.reset_position()
        board.l_point()
        
    #Detect L paddle miss
    if the_Ball.xcor() < -380:
        the_Ball.reset_position()
        board.r_point()





screen.exitonclick()