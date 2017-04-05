import turtle

size = 0.1

turtle.shape("turtle")
turtle.color(255/255,153/255,255/255)
turtle.pensize(10)

for _ in range(3600):
    turtle.forward(size)
    turtle.left(0.1)

