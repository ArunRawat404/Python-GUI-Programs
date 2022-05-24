from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()  # Inheriting properties of turtle class
        self.shape("circle")  # we can now directly use turtle class method and attribute using .self
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):  # for generating food to new location
        random_x_coordinate = random.randint(-275, 270)
        random_y_coordinate = random.randint(-275, 275)
        self.goto(random_x_coordinate, random_y_coordinate)
