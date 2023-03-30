from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-200,250)
        self.write("Level: ",align = "center", font=FONT)
        self.goto(-130,250)
        self.write(self.game_score, align = "center", font=FONT)
        
    def update_game_score(self):
        self.game_score += 1
        self.update_scoreboard()

    def game_over(self):
        #t= Turtle()
        self.penup()
        self.goto(0,0)
        self.write("Game Over",align = "center", font=FONT)
        

       