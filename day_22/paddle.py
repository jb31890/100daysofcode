from turtle import Turtle

UP = 90
DOWN = 270
PADDLE_SIZE = (20, 100, 1)


class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.create_paddle(starting_pos)
        
    def create_paddle(self, starting_pos):
        #self.resizemode("user")
        #self.shapesize(PADDLE_SIZE)
        self.shape("square")
        self.shapesize(1, 5, .1)
        self.seth(UP)
        self.pu()
        self.speed("fastest")
        self.color("white")
        self.goto(starting_pos)

    def up(self):
        if self.ycor() <= 240:
            self.seth(UP)
            self.forward(20)

    def down(self):
        if self.ycor() >= -220:
            self.seth(DOWN)
            self.forward(20)
