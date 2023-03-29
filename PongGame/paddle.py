from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,startingPosition):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1,None)
        self.startPos = startingPosition
        self.create_pong()
        
        
    def create_pong(self):
        self.penup()
        self.goto(self.startPos)
       
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


        

    