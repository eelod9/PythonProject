from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.tlist = []
        self.create_snake()
        self.head = self.tlist[0]
        
    def create_snake(self):
        for t in STARTING_POSITIONS:
            self.add_segment(t)
            
    
    def add_segment(self,position):   
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.tlist.append(t)
    
    def reset(self):
        for seg in self.tlist:
            seg.goto(1000,1000)
        self.tlist.clear()
        self.create_snake()
        self.head = self.tlist[0]
        

    def extend(self):
        self.add_segment(self.tlist[-1].position())


    def move(self):
        for seg_num in range(len(self.tlist)-1,0,-1):
            new_x = self.tlist[seg_num - 1].xcor()
            new_y = self.tlist[seg_num - 1].ycor()
            self.tlist[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
       if self.head.heading() != UP: 
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
       

    