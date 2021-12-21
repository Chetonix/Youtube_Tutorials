import turtle

chetonix = turtle.Pen()

chetonix.shape("turtle")

for i in range(6):
    chetonix.circle(100)
    chetonix.left(60)


chetonix.reset()
for i in range(8):
    chetonix.forward(100)
    chetonix.left(225)

input()