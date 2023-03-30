import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
myTurtle = Player()
board = Scoreboard()


car_manager = CarManager()

screen.listen()
screen.onkey(myTurtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
        
    #detect car collision
    for car in car_manager.all_cars:
        if myTurtle.distance(car) < 20:
            board.game_over()
            game_is_on = False
            

    #detect if reached end successfully
    if myTurtle.check_finished():
        #print("finished")
        car_manager.level_up()
        myTurtle.restart()
        board.update_game_score()




    





screen.exitonclick()
    
