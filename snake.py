from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.x = 0
        for _ in range(3):
            self.add_segment(self.x, 0)
            self.x -= 20

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            # move the last segment to the next one, so that it follows the position of first segment
            # and change direction accordingly
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, new_x, new_y):
        turtle_obj = Turtle(shape="square")
        turtle_obj.penup()
        turtle_obj.color("white")
        turtle_obj.goto((new_x, new_y))
        self.segments.append(turtle_obj)

    def extend(self):
        # since the last one will move one step ahead, we will add new segment on the position of the last segment
        self.add_segment(new_x=self.segments[-1].xcor(), new_y=self.segments[-1].ycor())

    def turn_up(self):
        # not to move in opposite
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
