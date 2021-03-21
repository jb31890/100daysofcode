from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.draw()

    def draw(self):
        self.ht()
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(-30,280)
        self.write(f"Score = {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.draw()