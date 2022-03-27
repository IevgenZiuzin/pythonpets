'''Capricorn December 22 to January 19
Aquarius January 20 to February 18
Pisces February 19 to March 20
Aries March 21 to April 19
Taurus April 20 to May 20
Gemini May 21 to June 20
Cancer June 21 to July 22
Leo July 23 to August 22
Virgo August 23 to September 22
Libra September 23 to October 22
Scorpio October 23 to November 21
Sagittarius November 22 to December 21'''

"""chinese_signs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']

while True:

    month = input('Type month: ')
    date = int(input('Type date: '))
    year = int(input('Type year: '))

    if month == 'December' and date > 22 or month == 'January' and date < 19:
        sign = 'Capricorn'
    elif month == 'January' and date > 20 or month == 'February' and date < 18:
        sign = 'Aquarius'
    elif month == 'February' and date > 19 or month == 'March' and date < 20:
        sign = 'Pisces'
    elif month == 'March' and date > 21 or month == 'April' and date < 19:
        sign = 'Aries'
    elif month == 'April' and date > 20 or month == 'May' and date < 20:
        sign = 'Taurus'
    elif month == 'May' and date > 21 or month == 'June' and date < 20:
        sign = 'Gemini'
    elif month == 'June' and date > 21 or month == 'July' and date < 22:
        sign = 'Cancer'
    elif month == 'July' and date > 23 or month == 'August' and date < 22:
        sign = 'Leo'
    elif month == 'August' and date > 23 or month == 'September' and date < 22:
        sign = 'Virgo'
    elif month == 'September' and date > 23 or month == 'October' and date < 21:
        sign = 'Libra'
    elif month == 'October' and date > 22 or month == 'November' and date < 21:
        sign = 'Scorpio'
    elif month == 'November' and date > 22 or month == 'December' and date < 19:
        sign = 'Sagittarius'

    for c in range (len(chinese_signs)):
        if year % 12 == c:
            year_sign = chinese_signs[c]

    print('This date is for %s, year of %s' % (sign, year_sign))"""

"""while True:
    mag = float(input('Enter magnitude to check it Richter scale: '))

    if mag < 2:
        dscrpt = 'Micro'
    elif mag >= 2 and mag < 3:
        dscrptr = 'Very minor'
    elif mag >= 3 and mag < 4:
        dscrptr = 'Minor'
    elif mag >= 4 and mag < 5:
        dscrptr = 'Light'
    elif mag >= 5 and mag < 6:
        dscrptr = 'Moderate'
    elif mag >= 6 and mag < 7:
        dscrptr = 'Strong'
    elif mag >= 7 and mag < 8:
        dscrptr = 'Major'
    elif mag >= 8 and mag < 10:
        dscrptr = 'Great'
    elif mag > 10:
        dscrptr = 'Meteoric'

    print('This magnitude is associated with "%s" earthquake level in Richter scale' % (dscrptr))"""


"""a_plus = 4.0
a = 4.0
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0

letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
numeral_grades = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]


while True:

    letter = input('Type grade letter to see its numeral value: ')

    if letter not in letter_grades:
        print('Wrong input')
    else:
        for c in range(len(letter_grades)):
            if letter == letter_grades[c]:
                numeral = numeral_grades[c]
        print('Grade \'%s\' is the same as \'%.1f\'' % (letter, numeral))"""


"""letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
numeral_grades = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
letter_grades_r = letter_grades[::-1]
numeral_grades_r = numeral_grades[::-1]
limit = 0.3


while True:
    grade = float(input('Type numeral grade to see its letter correspondence: '))
    if grade < 0 or grade > 4.3:
        print('Wrong input. Should be from 0 to 4,3.')
    else:
        for c in range (len(letter_grades_r)):
            if grade >= numeral_grades_r[c] and grade < numeral_grades_r[c] + limit:
                letter = letter_grades_r[c]
        print('This grade corresponds to \'%s\'.' % (letter))"""

"""bonus = 2400
low_rate = 0
middle_rate = 0.4
high_rate = 0.6
rate = float(input('Type your rate: '))

if rate == low_rate:
    amount = bonus * low_rate
    print(amount)
elif rate == middle_rate:
    amount = bonus * middle_rate
    print(amount)
elif rate >= high_rate:
    amount = bonus * rate
    print(amount)
else:
    print('Wrong input')"""

"""plan_price = 15

fee_911 = 0.44
added_minutes_price = 0.25
added_sms_price = 0.15
tax = 0.05

minutes_limit = 50
sms_limit = 50

added_minutes = 0
added_sms = 0

minutes, sms = map(int, (input('Type used minutes and sms amounts using SPACE between them: ')).split())

if minutes > minutes_limit:
    added_minutes = minutes - minutes_limit
if sms > sms_limit:
    added_sms = sms - sms_limit

added_minutes_cost = added_minutes_price * added_minutes
added_sms_cost = added_sms * added_sms_price

tax_costs = (plan_price + added_minutes_cost + added_sms_cost + fee_911) * tax
netto = plan_price + added_minutes_cost + added_sms_cost
total = netto + fee_911 + tax_costs

print('\nYour plan price: %.2f (%d minutes, %d sms)' % (plan_price, minutes_limit, sms_limit))
if added_minutes_cost > 0:
    print('Additional minutes: %.2f (%.2f per minute)' % (added_minutes_cost, added_minutes_price))
if added_sms_cost > 0:
    print('Additional sms: %.2f (%.2f per sms)' % (added_sms_cost, added_sms_price))
print('NETTO: %2.2f\n911 fee: %.2f\nTax costs: %.2f (%d%s)\nTOTAL: %.2f' % (netto, fee_911, tax_costs, tax * 100, '%', total))"""

"""while True:
    year = int(input('Type year to check is it leap or not: '))
    if year % 400 == 0:
        leap = 'is'
    else:
        if year % 100 == 0:
            leap = 'is not'
        elif year % 4 == 0:
            leap = 'is'
        else:
            leap = 'is not'
    print('This year %s leap' % (leap))"""
'''while True:
    year, month, day = map(int, input('Type year, month and day using SPACE between them:').split())
    if year % 400 == 0:
        leap = True
    else:
        if year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        else:
            leap = False
    if month == 12 and day == 31:
        year += 1
    if day == 31 and month in (1, 3, 5, 7, 8, 10):
        day = 1
        month += 1
    elif day == 30 and month in (4, 6, 9, 11):
        day = 1
        month += 1
    elif day >= 1 and day < 30:
        if month == 2 and day == 28:
            if leap:
                day += 1
            else:
                day = 1
                month += 1
        else:
            day += 1
    if day == 31 and month == 12:
        day = 1
        month = 1
    if month < 1 or month > 12 or day < 1 or (day > 30 and month not in (4, 6, 9, 11)) or day > 31 or (
            day > 28 and month == 2 and not leap) or (day > 29 and month == 2 and leap):
        print('Wrong Input')
    else:
        print(year, month, day)'''
"""import math
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
while True:
    year = int(input('Type year to check its first week day: '))
    day = (year + math.floor((year -1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7
    for c in range (len(days)):
        if day == c:
            week_day = days[c]
    print('Year %d has began on %s.' % (year, week_day))"""

"""import random
import time

numbers = [c for c in range(0, 37)]
numbers.append('00')
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
while True:
    number = random.choice(numbers)
    start = input('Press ENTER to start: ')
    time.sleep(2)
    print('\nThe spin resulted in', number)
    print('Pay', number)
    if number == 0 or number == '00':
        continue
    if number in reds:
        print('Pay Red')
    else:
        print('Pay Black')
    if number % 2 == 0:
        print('Pay Even')
    else:
        print('Pay Odd')
    if number >= 1 and number <= 18:
        range = '1 to 18\n'
    else:
        range = '19 to 36\n'
    print('Pay', range)"""

"""sum = 0
members = -1
number = 0
while number != '':
    sum += float(number)
    number = input('Type number: ')
    members += 1
print(sum / members)"""

"""old_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 0.6
new_prices = []
for c in range(len(old_prices)):
    new_price = (old_prices[c] * discount)
    new_prices.append(round(new_price, 2))
print('Old prices: ' + str(old_prices) + '\n' + 'New prices: ' + str(new_prices) + '\n' + 'Discount: ' + str(round(discount * 100)) + '%')"""

"""celcius = [c for c in range(-100, 110, 10)]
farenheit = []
for c in range(len(celcius)):
    far = round((celcius[c] * (9 / 5) + 32))
    farenheit.append(far)
print(str(celcius) + '\n' + str(farenheit))"""

"""price = 0
total = 0
lowest_coin = 5
while price != '':
    total += float(price) * 100
    price = input('Type price 0.00 form: ')
remainder = total - ((total // lowest_coin) * lowest_coin)
to_pay = (total - remainder) / 100
print(total)
print(remainder)
print(to_pay)"""

"""letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
numeral_grades = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]

letter = input('Type grade letter: ')
total = 0
grades_number = 0
while letter != '':
    for c in range(len(letter_grades)):
        if letter == letter_grades[c]:
            total += numeral_grades[c]
            grades_number += 1
    letter = input('Type grade letter: ')
print(total)
print(grades_number)
print('Average grade is %.2f' % (total / grades_number))"""

"""babies = [n for n in range(0,3)]
children = [n for n in range(3, 12)]
adults = [n for n in range(12, 65)]
oldies = [n for n in range(65, 121)]

babies_price = 0
children_price = 14
adults_price = 23
oldies_price = 18

total = 0

age = input('Your age, please: ')
while age != '':
    if int(age) in babies:
        total += babies_price
    if int(age) in children:
        total += children_price
    if int(age) in adults:
        total += adults_price
    if int(age) in oldies:
        total += oldies_price
    age = input('Your age, please: ')

print('Total: %.2f dollars.' % (total))"""

import random
alphabet = "abcdefghijklnmopqrstuvwxyz"
randomstring = ""
while len(randomstring) < 6:
    i = random.randint(0, len(alphabet))
    randomstring = randomstring + alphabet[i]
print(randomstring)
