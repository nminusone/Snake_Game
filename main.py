import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Create a snake body -create 3 snake bodies starting from 0,0 and going back, body is 20x20
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# segment_2 = Turtle(shape='square')
# segment_2.color('white')
# segment_2.goto(x=-20, y=0)
# segment_3 = Turtle(shape='square')
# segment_3.color('white')
# segment_3.goto(x=-40, y=0)
screen.exitonclick()
