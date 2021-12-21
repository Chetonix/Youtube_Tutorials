import turtle
import random

chetonix = turtle.Pen()

chetonix.shape("turtle")
chetonix.speed(0)
color_list = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
chetonix.width(5)
def circle(size):
    chetonix.circle(size)

for i in range(100):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    chetonix.up()
    chetonix.goto(x,y)
    chetonix.down()
    color = random.choice(color_list)
    chetonix.color(color)
    chetonix.circle(random.randrange(-200, 200))

input()