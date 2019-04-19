from turtle import Turtle
kame = Turtle()
kame.up()
kame.goto(200,200)
kame.down()
for i in range(5):
    for j in range(5):
        kame.right(72)
        kame.fd(i*100)
kame.right(126)
kame.fd(1000)
