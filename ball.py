# from display import MyWindow
# from random import randint
from turtle import Turtle

BALL_SHAPE = "circle"
BALL_COLOR = "#FFFFFF"


# class Ball
class Ball(Turtle):
    """class Ball
    Instance:
    x_position, y_position, ball_speed
    Method:
    move_ball, collision_wall, collision_paddle, refresh_ball
    """
    def __init__(self):
        super().__init__()
        self.list_of_ball = []
        self.penup()
        self.setheading(90)
        self.shape(BALL_SHAPE)
        self.goto(0, 0)
        # random position
        # self.goto(0, randint(-MyWindow().y_coord+40, MyWindow().y_coord-40))
        self.color(BALL_COLOR)
        self.shapesize(1, 1)
        self.x_position = 10
        self.y_position = 10
        self.ball_speed = 0.1

    # Method to move ball
    def move_ball(self):
        """Method to move ball"""
        xposition = self.xcor() + self.x_position
        yposition = self.ycor() + self.y_position
        self.goto(xposition, yposition)

    # Method to change bonce of ball when boll collision with wall
    def collision_wall(self):
        """Method to change bonce of ball when boll collision with wall"""
        self.y_position *= -1

    # Method to change bonce of ball when boll collision with paddle
    def collision_paddle(self):
        """Method to change bonce of ball when boll collision with paddle"""
        self.x_position *= -1
        self.ball_speed *= 0.9

    # Method to refresh ball in (0,0) coordinate
    def refresh_ball(self):
        """Method to refresh ball in (0,0) coordinate"""
        self.goto(0, 0)
        # random position
        # self.goto(0, randint(-MyWindow().y_coord+40, MyWindow().y_coord-40))
        self.ball_speed = 0.1
        self.x_position *= -1
