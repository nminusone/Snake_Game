from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.write(f"Scoreboard:{self.scores}", move=False, align='center', font=('Arial', 10, 'normal'))

    def change(self):
        self.clear()
        self.scores += 1
        self.write(f"Scoreboard:{self.scores}", move=False, align='center', font=('Arial', 10, 'normal'))

