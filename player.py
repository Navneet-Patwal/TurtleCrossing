from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.goto(STARTING_POINT)
        self.setheading(90)
        self.color("black")
        self.shape("turtle")

    def start(self):
        self.goto(STARTING_POINT)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finished(self):
        if self.ycor() > 280:
            return True
        else:
            return False


