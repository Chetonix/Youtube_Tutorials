import turtle

chetonix = turtle.Pen()

chetonix.shape("turtle")
chetonix.speed(0)
chetonix.color("red")
chetonix.width(4)
for i in range(20):
    chetonix.circle(i*3, 180)
    chetonix.right(45)




input()