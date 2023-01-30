from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("score_track.txt") as file:
            data = file.read()

        self.highest_score = data
        self.penup()
        self.hideturtle()
        self.color("gold")
        self.goto(0, 250)
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self, score):
        self.clear()
        self.score += score
        self.display_score()

    def game_over(self):
        if self.score > int(self.highest_score):
            with open("score_track.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.goto(0, -100)
        self.color("firebrick")
        self.write("Game Over!", move=False, align=ALIGNMENT, font=("courier", 30, "bold"))

    def game_won(self):
        if self.score > int(self.highest_score):
            with open("score_track.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.goto(0, -100)
        self.color("gold")
        self.write("You Won the Game!", move=False, align=ALIGNMENT, font=("courier", 30, "bold"))
