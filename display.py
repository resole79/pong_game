from turtle import Screen

# Declare variable and CONSTANT
X_SCREEN = 800
Y_SCREEN = 600
SCREEN_COLOR = "#000000"
SCREEN_TITLE = "Pong Game"

x_coordinate = X_SCREEN // 2
y_coordinate = Y_SCREEN // 2


# Class MyWindow
class MyWindow:
    """Class MyWindow
    # Instance
    window_list, this_window, x_coord, y_coord
    Method:
    create_window
    """
    def __init__(self):
        self.window_list = []
        self.create_window()
        self.x_coord = x_coordinate
        self.y_coord = y_coordinate
        self.this_window = self.window_list[0]

    # Method to create window
    def create_window(self):
        """Method to create window"""
        window = Screen()
        window.colormode(255)
        window.title(SCREEN_TITLE)
        window.bgcolor(SCREEN_COLOR)
        window.setup(X_SCREEN, Y_SCREEN)
        window.tracer(0)
        self.window_list.append(window)
