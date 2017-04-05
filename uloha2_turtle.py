import turtle as t

n = 1
size = 100

t.penup()
t.goto(-size/2, size/10 * n/2)
t.pendown()
#t.rgb(102, 153, 153)

t.shape("turtle")

for i in range(n):
    t.forward(size)
    t.right(90)
    t.forward(size/10)
    t.right(90)
    t.forward(size)
    t.left(90)
    t.forward(size/10)
    t.left(90)
