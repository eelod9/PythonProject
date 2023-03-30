from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.restart()
        
        
    def restart(self):
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)
        self.check_finished()
    
    def check_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
