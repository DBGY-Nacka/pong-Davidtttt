from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(1)
        self.dx = random.choice([10, -10])
        self.dy = random.choice([10, -10])
        self.speed_increase_factor = 1.05

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1
        self.increase_speed()

    def bounce_x(self):
        self.dx *= -1
        self.increase_speed()

    def increase_speed(self):
        self.dx *= self.speed_increase_factor
        self.dy *= self.speed_increase_factor

    def reset_position(self):
        self.goto(0, 0)
        self.dx = random.choice([10, -10])
        self.dy = random.choice([10, -10])
