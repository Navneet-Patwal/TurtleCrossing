
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
import time
from car_manager import CarManager
screen = Screen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move, key="Up")
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    #detect collison with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    #detect successful crossing
    if player.finished():
        player.start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()

