from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.draw()

    def draw(self):
        self.ht()
        self.pu()
        self.speed("fastest")
        self.color("black")
        self.goto(-280,270)
        self.write(f"Level: {self.level}", align="left", font=(FONT))
    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.draw()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=(FONT))
