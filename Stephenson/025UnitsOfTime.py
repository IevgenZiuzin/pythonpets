"""Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary."""

while True:
    seconds_amount = int(input('Type seconds amount: '))
    days = seconds_amount // 86400
    hours = (seconds_amount % 86400) // 3600
    minutes = ((seconds_amount % 86400) % 3600) // 60
    seconds = ((seconds_amount % 86400) % 3600) % 60
    print('It equals {:02d} days : {:02d} hours : {:02d} minutes : {:02d} seconds'.format(days, hours, minutes, seconds))