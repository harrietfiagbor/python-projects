from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from divider import Divider
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = Ball()
score = Scoreboard()
divider = Divider()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # increase left score
        score.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        # increase right score
        score.r_point()

screen.exitonclick()

# TODO 1. create screen. Make it black. set dimension to be width=800 and height=600
# TODO 2. create paddle of width 100 and height 20 and cause it to move vertically on the screen. that is, up and down
# TODO 3. create another paddle and cause it to also move with with the w and s keys, up and down
# TODO 4. Create a ball and cause it to move across the screen
# TODO 5. Detect Collision with wall and bounce back
# TODO 6. Detect Collision with paddles and bounce back
# TODO 7. Detect when Paddle misses
# TODO 8. Keep Score
