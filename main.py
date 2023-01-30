from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle(0, -280)
ball = Ball()
scoreboard = Scoreboard()

all_bricks = []
brick_xcor = -360
brick_ycor = 200
for _ in range(9):
    for _ in range(12):
        brick = Brick(brick_xcor, brick_ycor)
        all_bricks.append(brick)
        brick_xcor += 65
    brick_xcor = -360
    brick_ycor -= 25

screen.listen()
screen.onkey(fun=paddle.move_right, key="Right")
screen.onkey(fun=paddle.move_left, key="Left")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -280:
        game_on = False
        scoreboard.game_over()
        ball.bounce_y()
    elif ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    elif ball.distance(paddle) < 45 and ball.ycor() < -250:
        ball.bounce_y()
    elif ball.ycor() > 250:
        ball.bounce_y()

    for brick in all_bricks:
        total_bricks = len(all_bricks)
        if ball.distance(brick) < 45:
            brick.goto(3000, 3000)
            all_bricks.remove(brick)
            score = total_bricks - len(all_bricks)
            scoreboard.increase_score(score)

            if ball.xcor() < brick.left_wall:
                ball.bounce_x()
            elif ball.xcor() > brick.right_wall:
                ball.bounce_x()
            elif ball.ycor() > brick.upper_wall:
                ball.bounce_y()
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce_y()

            if score == total_bricks:
                game_on = False
                scoreboard.game_won()

screen.exitonclick()
