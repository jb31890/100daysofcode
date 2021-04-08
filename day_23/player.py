from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()
        
    def create_player(self):
        self.shape("turtle")
        self.seth(UP)
        self.pu()
        self.speed("fastest")
        self.color("black")
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(20)

    def reset(self):
        self.goto(STARTING_POSITION)

