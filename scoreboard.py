from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)

    def level_up(self):
        self.level += 1
        self.clear()
        self.display()

    def display(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
