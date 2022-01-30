# Star is made using 6 colours

import turtle

sc = turtle.Screen()
sc.setup(800, 600)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("pink")
col = ("yellow", "blue", "orange", "green", "red", "purple")
c = 0
for i in range(80):
    spiral.forward(i * 10)
    spiral.right(144)
    spiral.color(col[c])
    c += 1
    if c == 4:
        c = 0
