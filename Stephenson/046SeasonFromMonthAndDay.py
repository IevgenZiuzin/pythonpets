"""The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:
Season      First day
Spring      March 20
Summer      June 21
Fall        September 22
Winter      December 21
Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered."""

while True:
    month = input('Type month: ')
    date = int(input('Type date: '))
    if month == 'January' or month == 'February':
        season = 'winter'
    elif month == 'March':
        if date < 20:
            season = 'winter'
        else:
            season = 'spring'
    elif month == 'April' or month == 'May':
        season = 'spring'
    elif month == 'June':
        if date < 21:
            season = 'spring'
        else:
            season = 'summer'
    elif month == 'July' or month == 'August':
        season = 'summer'
    elif month == 'September':
        if date < 22:
            season = 'summer'
        else:
            season = 'autumn'
    elif month == 'October' or month == 'November':
        season = 'autumn'
    elif month == 'December':
        if date < 21:
            season = 'autumn'
        else:
            season = 'winter'
    print('%s is associated with this date' % (season))