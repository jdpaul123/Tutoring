# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
t.speed('fastest')
turtle.bgcolor("black")
sides = 4
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for x in range(360):
    # print(x)
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
