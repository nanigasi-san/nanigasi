from turtle import Turtle
from time import sleep
from random import choice
length = 0
kame = Turtle()
color_list = ["red","blue","green","black"]
while True:
    length += 1
    kame.forward(length)
    kame.right(90)
    kame.color(choice(color_list))