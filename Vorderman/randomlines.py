import random
import turtle as t

def get_line_length():
    choice = input('Choose line length (1/2/3): ')
    if choice == '1':
        line_length = 100
    elif choice == '2':
        line_length = 200
    elif choice == '3':
        line_length = 250
    return line_length

def get_line_width():
    choice = input('Choose line width (4/5/6): ')
    if choice == '4':
        line_width = 10
    elif choice == '5':
        line_width = 25
    elif choice == '6':
        line_width = 40
    return line_width

def inside_window():
    left_limit = (-t.window_width() / 3) + 100
    right_limit = (t.window_width() / 3) - 100
    top_limit = (t.window_height() / 3) - 100
    bottom_limit = (-t.window_height() / 3) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle(line_length):
    pen_colors = ['red', 'orange', 'yellow', 'green', \
                  'blue', 'purple']
    t.pencolor(random.choice(pen_colors))
    if inside_window():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)

line_length = get_line_length()
line_width = get_line_width()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width)

while True:
    move_turtle(line_length)
    
