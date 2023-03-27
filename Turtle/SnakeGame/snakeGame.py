from turtle import Screen
import time
from snakeClass import Snake
from food import Food
from scoreBoard import Score
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
tlist = []
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()
    
    #Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        game_is_on =False #end of game
        scoreBoard.game_over()
    
    #Detect collision with tail.
    #if head collides with any segment in tail: trigger game_over
    for t in tlist[1:]:
        if snake.head.distance(t) < 10:
            game_is_on = False
            scoreBoard.game_over()
        

        












screen.exitonclick()