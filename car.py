import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'blue', 'purple', 'cyan', 'green']


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.move_speed = 10
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setup()

    def setup(self):
        start_pos_y = random.randint(-200, 200)
        start_pos_x = 320
        self.color(random.choice(COLORS))
        self.goto(start_pos_x, start_pos_y)

    def move(self):
        self.setx(self.xcor() - self.move_speed)
