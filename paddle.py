from display import MyWindow
from turtle import Turtle

# Declare variable and CONSTANT
up = 90
down = 270
SHAPE_PADDLE = "square"
PADDLE_COLOR = "#FFFFFF"


# Class Paddle
class Paddle(Turtle):
    """Class Paddle
    Method:
    move_paddle, paddle_up, paddle_down
    """
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(SHAPE_PADDLE)
        self.setheading(90)
        self.color(PADDLE_COLOR)
        self.shapesize(1, 5)
        self.goto(position)

    # Method to move paddle
    def move_paddle(self):
        """Method to move paddle"""
        # if "ycor" of paddle is equal to end of screen
        # paddle come back and continuous to forward
        if self.ycor() == MyWindow().y_coord - 40:
            self.setheading(270)
            self.forward(20)
        elif self.ycor() == -MyWindow().y_coord + 40:
            self.setheading(90)
            self.forward(20)
        else:
            self.forward(20)

    def paddle_up(self):
        self.setheading(up)
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)

    def paddle_down(self):
        self.setheading(down)
        # new_y = self.ycor() - 20
        # self.goto(self.xcor(), new_y)
