from turtle import Turtle

SPEED = 1.25


class Ball(Turtle):
    """A class to represent a ball in the game Pong."""

    def __init__(self):
        """Initialize attributes for the ball."""
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.ball_speed = 0.1
        self.x_move = 13
        self.y_move = 5

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Determines the y coordinates for the ball after it bounces against
        a surface."""
        self.y_move *= -1

    def bounce_x(self):
        """Determines the x coordinates for the ball after it bounces against
        a surface."""
        self.x_move *= -1
        self.ball_speed *= 0.95

    def reset_ball(self):
        """Resets the ball to its original position and reverses the
        direction it heads in."""
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1

    def increase_speed(self):
        """Increase the speed of the ball."""
        self.speed("fastest")
