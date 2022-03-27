import turtle as t
from random import randint, random
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

#Main code
t.Screen().bgcolor('black')
t.hideturtle()

while True:
    randPts = randint(3, 15) * 2 + 1
    randSize = randint(10, 100)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    draw_star(randPts, randSize, next(colors), ranX, ranY)





