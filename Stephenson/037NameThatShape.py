"""Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message."""

figures = ['triangle', 'quadrangle', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']
while True:
    sides_amount = int(input('Enter sides amount of your figure: ')) - 3
    if sides_amount >= 0 and sides_amount <= (len(figures) - 1) and figures[sides_amount]:
        print('It is ' + figures[sides_amount])
    else:
        print('Wrong number. Should be from 3 to 10.')