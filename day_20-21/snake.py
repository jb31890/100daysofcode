from turtle import Turtle 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POS = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self):
        self.snek = []
        self.create_snek()
        self.head = self.snek[0]

    def create_snek(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def extend(self):
        self.add_segment(self.snek[-1].position())

    def add_segment(self, pos):
        snek_piece = Turtle(shape="square")
        snek_piece.pu()
        snek_piece.speed("fastest")
        snek_piece.color("white")
        snek_piece.goto(pos)
        self.snek.append(snek_piece)

    def move(self):
        for seg in range(len(self.snek) - 1, 0, -1):
            new_x = self.snek[seg - 1].xcor()
            new_y = self.snek[seg - 1].ycor()
            self.snek[seg].goto(new_x,new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)