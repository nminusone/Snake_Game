from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.starting_pos:
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].seth(90)

    def down(self):
        self.segments[0].seth(270)

    def left(self):
        self.segments[0].seth(180)

    def right(self):
        self.segments[0].seth(0)
