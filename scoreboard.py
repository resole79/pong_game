from display import MyWindow
from turtle import Turtle

# Declare variable and CONSTANT
DISTANCE_FOR_SCORE = 60
GAME_OVER_IMAGE = "./image/pong.png"
FONT = ("Courier", 15, "bold")
ALIGN = "center"
SCOREBOARD_COLOR = "#FFFFFF"


# Class Scoreboard
class Scoreboard(Turtle):
    """
    Class Scoreboard
    Instance:
    score_my, score_pc
    Method:
    game_over, increase_score1, increase_score2,
    increase_score2, refresh_score
    """
    def __init__(self):
        super().__init__()
        self.score_my = 0
        self.score_pc = 0
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(0, MyWindow().y_coord - DISTANCE_FOR_SCORE)
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        MyWindow().this_window.bgpic(GAME_OVER_IMAGE)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score1(self):
        self.score_my += 15

    def increase_score2(self):
        self.score_pc += 15

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score_my} \t Score: {self.score_pc}", align=ALIGN, font=FONT)
