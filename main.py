# --------------- Initial color setup ---------------
# import colorgram

# rgb_colors =[]
# colors = colorgram.extract('spots.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.b
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# ----------------------------------------------------

import turtle
from turtle import Turtle, Screen
from random import choice

t = Turtle()
turtle.colormode(255)
size = 300
turtle.screensize(size, size)

color_list = [(207, 82, 82), (54, 130, 130), (145, 40, 40), (140, 49, 49), (221, 105, 105), (132, 203, 203),
              (158, 83, 83), (45, 104, 104), (169, 39, 39), (129, 143, 143), (83, 44, 44), (37, 67, 67),
              (186, 107, 107), (187, 170, 170), (85, 180, 180), (59, 31, 31), (88, 92, 92), (78, 165, 165),
              (194, 73, 73), (45, 78, 78), (80, 44, 44), (161, 218, 218), (57, 121, 121), (219, 187, 187),
              (169, 172, 172), (219, 169, 169)]

t.speed(0)
t.ht()
for x in range(0, size*2):
    if x % 60 == 0:
        t.penup()
        t.goto(-size, x - size)
        for _ in range(0, 10):
            t.pendown()
            t.dot(int(size/10), choice(color_list))
            t.penup()
            t.forward(int(size/5))

screen = Screen()
screen.exitonclick()
