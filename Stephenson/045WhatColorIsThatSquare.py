"""Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row.
Write a program that reads a position from the user. Use an if statement to determine
if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking."""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [n for n in range (1, 9)]
while True:
    field = input('Type a name of field on chess board to checks its color: ')
    letter = str(field[0])
    number = int(field[1])
    if letter not in letters or number not in numbers:
        print('Maybe, you are out off chess board')
    else:
        letter_index = letters.index(letter)
        number_index = numbers.index(number)
        if letter_index % 2 == number_index % 2:
            color = 'black'
        else:
            color = 'white'
        print('Field %s%d is %s.' % (letter, number, color))