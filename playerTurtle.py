from turtle import Turtle


class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -260)

    def move_up(self):
        self.sety(self.ycor() + 10)

    def move_down(self):
        self.sety(self.ycor() - 10)

    def reset(self):
        self.goto(0, -260)

    def touch_finish_line(self):
        return self.ycor() > 280

