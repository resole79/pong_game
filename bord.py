import display
from display import MyWindow
from turtle import Turtle

# Declare variable and CONSTANT
DISTANCE = 20
PENSIZE = 10
BORD_COLOR = "#AAAFFF"
RANGE_OF_BORD = display.MyWindow().y_coord // 10


# Class BordGame
class BordGame(Turtle):
    """ Class BordGame
    method:
    create_bord
    """
    def __init__(self):
        super().__init__()
        self.goto(0, MyWindow().y_coord)
        self.color(BORD_COLOR)
        self.pensize(PENSIZE)
        self.hideturtle()
        self.speed("fastest")

    # Method to create bord
    def create_bord(self):
        """Method to create bord"""
        # Create dash line
        self.setheading(270)
        for i in range(RANGE_OF_BORD):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

        self.penup()
        self.goto(-MyWindow().x_coord + 5, MyWindow().y_coord - 5)

        # create end lines
        for i in range(4):
            self.penup()
            self.forward(display.Y_SCREEN - DISTANCE)
            self.right(270)
            self.pendown()
            self.forward(display.X_SCREEN - DISTANCE)
            self.right(270)
