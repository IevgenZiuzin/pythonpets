"""Canada has three national holidays which fall on the same dates each year.
Holiday             Date
New year’s day      January 1
Canada day          July 1
Christmas day       December 25
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday."""

days = [1, 1, 25]
monthes = ['January', 'July', 'December']
holidays = ['New year\'s day', 'Canada day', 'Christmas day']
index = [n for n in range(len(days))]

while True:
    day = int(input('Type a day: '))
    month = input('Type month: ')
    if day == days[0] and month == monthes[0]:
            print('It is %s!' % (holidays[0]))
    elif day == days[1] and month == monthes[1]:
            print('It is %s!' % (holidays[1]))
    elif day == days[2] and month == monthes[2]:
            print('It is %s!' % (holidays[2]))
    else:
        print('This date does not correspond to fixed-day holidays.')