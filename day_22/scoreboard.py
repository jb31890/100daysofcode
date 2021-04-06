from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right = 0
        self.left = 0
        self.draw_midline()
        self.draw()

    def draw_midline(self):
        line = Turtle(shape="square")
        line.pu()
        line.color("white")
        line.ht()
        line.goto(0,280)
        line.seth(270)
        while line.ycor() > -280:
            line.pd()
            line.forward(5)
            line.pu()
            line.forward(5)

    def draw(self):
        self.ht()
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(-50,200)
        self.write(f"{self.left}", align="center", font=("Arial", 80, "normal"))
        self.goto(50,200)
        self.write(f"{self.right}", align="center", font=("Arial", 80, "normal"))
    
    def increase_score(self):
        self.clear()
        self.draw()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center")
    
    
    
