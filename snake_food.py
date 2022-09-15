from turtle import Turtle
import random

# inherited Turtle class to use the functionality of turtle class without creating Turtle object
# used super() to initialize parent constructor


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        # shapesize works like length = original_length * stretch_len.....similarly width
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        set_x = random.randint(-280, 280)
        set_y = random.randint(-280, 280)
        self.goto(set_x, set_y)
