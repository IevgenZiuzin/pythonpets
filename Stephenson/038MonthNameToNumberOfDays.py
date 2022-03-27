"""The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed."""

monthes_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
monthes_30 = ['november', 'june', 'april', 'september']
february = 'february'

while True:
    month = input('Enter month: ')
    if month in monthes_31:
        print(month + ' has 31 days')
    elif month in monthes_30:
        print(month + ' has 30 days')
    elif month == february:
        print('February has 28 or 29 days')
    else:
        print('Wrong input')