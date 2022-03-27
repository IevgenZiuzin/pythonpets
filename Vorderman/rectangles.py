import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_shape(size, angle, shift, shape):
    next_shape = ''
    if shape == 'circle':
        for c in range(3):
            t.pencolor(next(colors))
            t.circle(size)
            t.right(angle)
            t.forward(shift)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size * 2)
            t.left(90)
        next_shape = 'circle'
    draw_shape(size, angle + 5, shift + 0, next_shape)

t.bgcolor('black')
t.speed('fast')
t.pensize(10)
draw_shape(30, 0, 3, 'circle')
