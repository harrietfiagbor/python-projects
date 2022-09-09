import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
screen.onkey(player.move_up, "Up")

car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # Detect player has reached finish line
    if player.is_at_finish_line():
        player.reset_position()
        score.level_up()
        car_manager.increase_speed()

    # Level Up
screen.exitonclick()
