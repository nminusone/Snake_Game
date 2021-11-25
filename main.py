from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
# Create a snake body -create 3 snake bodies starting from 0,0 and going back, body is 20x20
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
# for snakes in range(0, 3):
#     snake_body = Turtle(shape='square')
#     snake_body.color('white')
#     snake_body.goto(x=x_pos, y=0)
#     x_pos -= 20
for position in starting_pos:
    segment = Turtle(shape='square')
    segment.color('white')
    segment.goto(position)

# segment_2 = Turtle(shape='square')
# segment_2.color('white')
# segment_2.goto(x=-20, y=0)
# segment_3 = Turtle(shape='square')
# segment_3.color('white')
# segment_3.goto(x=-40, y=0)
screen.exitonclick()
