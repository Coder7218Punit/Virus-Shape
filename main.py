import turtle
from turtle import *
t = turtle.Turtle()
speed(10)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

t.hideturtle()
turtle.done()
