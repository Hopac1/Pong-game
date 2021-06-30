from turtle import Turtle, Screen
from ball import Ball
from score import Score
import time
import random

# Constants
WIDTH = 600
HEIGHT = 600
POSITION_A = (-290, 0)
POSITION_B = (280, 0)

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title(titlestring="Pong Game")
screen.tracer(0)


ball = Ball()
score = Score()

# Create first paddle
paddle_a = Turtle("square")
paddle_a.color('white')
paddle_a.shapesize(4, 1)
paddle_a.speed("fastest")
paddle_a.penup()
paddle_a.goto(POSITION_A)

# Create second paddle
paddle_b = Turtle("square")
paddle_b.color('white')
paddle_b.shapesize(4, 0.9)
paddle_b.speed("fastest")
paddle_b.penup()
paddle_b.goto(POSITION_B)


# Define paddle movement
def paddle_a_up():
    """Moves paddle a upwards."""
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    """Moves paddle a upwards."""
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    """Moves paddle a upwards."""
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)


def paddle_b_down():
    """Moves paddle a upwards."""
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


# Enable keyboard controls
screen.listen()
screen.onkeypress(fun=paddle_a_up, key='w')
screen.onkeypress(fun=paddle_a_down, key='s')

screen.onkeypress(fun=paddle_b_up, key='Up')
screen.onkeypress(fun=paddle_b_down, key='Down')

# Create the ball and make it move
random_x = random.randint(70, 72)
random_y = random.randint(70, 81)

# Make bounce_y logic
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 260 and ball.distance(paddle_b) < 50 or ball.xcor() \
            < -260 and ball.distance(paddle_a) < 50:
        ball.increase_speed()
        ball.bounce_x()

    # Detect if paddle a missed the ball
    elif ball.xcor() < -295:
        score.add_b_score()
        ball.reset_ball()
        time.sleep(1)

    # Detect if paddle b missed the ball
    elif ball.xcor() > 287:
        score.add_a_score()
        ball.reset_ball()
        time.sleep(1)

screen.exitonclick()
