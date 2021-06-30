from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.a_score = 0
        self.b_score = 0
        self.update_score()

    def update_score(self):
        """Updates the score to the current score."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.a_score, align="center",
                   font=('Courier', 75, "normal"))
        self.goto(100, 200)
        self.write(self.b_score, align="center",
                   font=('Courier', 75, "normal"))

    def add_a_score(self):
        """Add 1 to add_a_score."""
        self.a_score += 1
        self.update_score()

    def add_b_score(self):
        """Add 1 to add_b_score."""
        self.b_score += 1
        self.update_score()
