import time
from turtle import Screen
from cars import Cars
from playerTurtle import PlayerTurtle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = PlayerTurtle()
screen.onkeypress(turtle.move_up, "Up")
screen.onkeypress(turtle.move_down, "Down")

cars = Cars()
scoreboard = Scoreboard()
scoreboard.display()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    cars.create_car()
    screen.update()

    for car in cars.cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # finish line
    if turtle.touch_finish_line():
        scoreboard.level_up()
        cars.update_speed()
        turtle.reset()

screen.exitonclick()
