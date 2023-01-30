from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x ,y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("cornflower blue")
        self.penup()
        self.goto(x, y)

    def move_right(self):
        new_x = self.xcor() + 20
        if self.xcor() < 350:
            self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        if self.xcor() > -350:
            self.goto(new_x, self.ycor())

