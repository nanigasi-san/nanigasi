from turtle import Turtle
import random
kame = Turtle()
color_list = ["red","blue","green"]
n = 0
while True:
    # kame.color(random.choice(color_list))
    kame.fd(n)
    kame.right(90)
    n += 0.1
