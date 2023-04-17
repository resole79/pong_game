from scoreboard import Scoreboard
from display import MyWindow
from bord import BordGame
from paddle import Paddle
from ball import Ball
import time

# Declare variable and CONSTANT
game_on = True
up_pc = "Left"
down_pc = "Right"
up = "a"
down = "d"

# call class and initialize "MyWindow", "BordGame", "Paddle", "Ball", Scoreboard
new_screen = MyWindow()
new_bord = BordGame()
new_ball = Ball()
new_scoreboard = Scoreboard()

my_paddle_initialize = (-new_screen.x_coord + 50, 0)
pc_paddle_initialize = (new_screen.x_coord - 50, 0)
my_paddle = Paddle(my_paddle_initialize)
pc_paddle = Paddle(pc_paddle_initialize)

# Create bord
new_bord.create_bord()

# listen onkey press
new_screen.this_window.listen()
new_screen.this_window.onkey(my_paddle.paddle_up, up)
new_screen.this_window.onkey(my_paddle.paddle_down, down)
new_screen.this_window.onkey(pc_paddle.paddle_up, up_pc)
new_screen.this_window.onkey(pc_paddle.paddle_down, down_pc)

# Cycle "while" condition to exit game_on equal to false
while game_on:
	new_screen.this_window.update()
	time.sleep(new_ball.ball_speed)

	my_paddle.move_paddle()
	pc_paddle.move_paddle()
	new_ball.move_ball()

	# "If" to check collision with wall
	if int(new_ball.ycor()) > MyWindow().y_coord - 20 or int(new_ball.ycor()) < -MyWindow().y_coord + 20:
		new_ball.collision_wall()

	# "If" to check collision with paddle
	if new_ball.distance(my_paddle) <= 50 and new_ball.xcor() < -MyWindow().x_coord + 80 \
		or new_ball.distance(pc_paddle) <= 50 and new_ball.xcor() > MyWindow().x_coord - 80:
		new_ball.collision_paddle()

	# "if" to check the ball are end of screen
	if new_ball.xcor() > MyWindow().x_coord - 20:
		new_scoreboard.increase_score1()
		new_ball.refresh_ball()
		new_scoreboard.refresh_score()
	if new_ball.xcor() < -MyWindow().x_coord + 20:
		new_scoreboard.increase_score2()
		new_ball.refresh_ball()
		new_scoreboard.refresh_score()

	# "if" to check score
	if new_scoreboard.score_my > 45 or new_scoreboard.score_pc > 45:
		new_scoreboard.game_over()
		game_on = False
	else:
		game_on = True

new_screen.this_window.exitonclick()
