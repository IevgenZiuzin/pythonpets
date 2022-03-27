"""import random

def guessing_game():
    number = random.randint(1, 100)
    while True:
        guess = int(input('Guess number: '))
        if guess == number:
            print('Yeah! It was ' + str(number))
            break
        else:
            if guess > number:
                print(f'Your guess of {guess} is too high!')
            else:
                print(f'Your guess of {guess} is too low!')

guessing_game()"""


"""                                    #EXERCISE 5

print('\n' + 'YOUR BACK-BOTTLES SUM' + '\n')

halfliter_price = 0.08
liter_price = 0.12

while True:
    bottles_number = int(input('Bottles: '))
    bottles_volume = input('Volume (0.5 or 1 l): ')
    if bottles_volume == '0.5':
        print('Sum to get: $' + '{0:.2f}'.format(bottles_number * halfliter_price))
    elif bottles_volume == '1':
        print('Sum to get: $' + '{0:.2f}'.format(bottles_number * liter_price))
    else:
        print('error')"""

"""
                                EXERCISE 6

print('\nRestaurant check\n')

tax_rate = 0.2
tip_rate = 0.1

cost = float(input('Type your cost of a meal: '))

tax_sum = cost * tax_rate
tip_sum = cost * tip_rate
total = cost + tax_sum + tip_sum

print('\nPOLYANA CHECK\n\nCost: %.2f\nTax: %.2f\nTip: %.2f\n\nTOTAL: %.2f' % (cost, tax_sum, tip_sum, total))"""



"""                                #EXERCISE 9
                                
deposit = float(input('Type your deposite: '))
yearly_rate = float(input('Type percent interest per year: '))
years_number = int(input('Type number of years: '))
current_year = int(input('Type current year: '))
for c in range(current_year + 1, current_year + years_number):
      yearly_earn = deposit * yearly_rate
      deposit = yearly_earn + deposit
      print(str(c) + (': %.2f' % (deposit)))"""

"""EXERCISE 10

while True:
      a, b = map(int, input('Type numbers using "SPACE" between them: ').split())
      print('SUM: %.d\nDIFF: %.f\nPRODUCT: %.f\nQUOTIENT: %.f\nREMAINDER: %.f\nRATE: %.f' % \
            ((a + b), (max(a, b) - min(a, b)), (a * b), (a / b), (a % b), (a ** b)))"""



"""                                #EXERCISE 11

kilometer_in_mile = 1.60934
liter_in_gallon = 3.785411784

while True:
    convert_direction = input('For MPG to L/100 km type "l". For L/100 to MPG type "m": ')
    efficiency = float(input('Type converted efficiency: '))
    if convert_direction == 'l':
        converted = (liter_in_gallon * 100) / (efficiency * kilometer_in_mile)
        print('%.1f Miles per Gallon equals %.1f Liter per 100 Kilometers' % (efficiency, converted))
    elif convert_direction == 'm':
        converted = ((100 / kilometer_in_mile) / (efficiency / liter_in_gallon))
        print('%.1f Liter per 100 Kilometers equals %.1f Miles per Gallon' % (efficiency, converted))
    else:
        print('error')"""






"""import random
import time

attempt = 0
user_score = 0
machine_score = 0
user_delay = 2
machine_delay = 2

while attempt > 3:
    start = input('Type ENTER to throw')
    time.sleep(user_delay)
    if start == '':
        user_throw = random.randint(1, 6)
        print('You throwed %.d' % (user_throw))
        time.sleep(user_delay)
        print('\nMy throw...')
        machine_throw = random.randint(1, 6)
        time.sleep(machine_delay * 2)
        print('I throwed %.d\n' %(machine_throw))
        if user_throw > machine_throw:
            user_score += 1
        elif machine_throw > user_throw:
            machine_score +=1
        else:
            print('Drawn\n')
        attempt += 1
        machine_delay += 1
    if attempt == 3:
        if user_score > machine_score:
            print('You %.d\nMe %.d\n\nYou win!' % (user_score, machine_score))
        if machine_score > user_score:
            print('You %.d\nMe %.d\n\nI win!' % (user_score, machine_score))
        if machine_score == user_score:
            print('Drawn Game. Continue')
            machine_delay = 2"""

"""import math
s1, s2, s3 = map(float, input('Type length of triangle sides using SPACE: ').split())
s = (s1 + s2 + s3) / 2
triangle_area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
print('Area of this triangle is %.2f square centimeters' % (triangle_area))"""

"""days, hours, minutes, seconds = map(int, input('Type days, hours, minutes and seconds using SPACE: ').split())

while True:
    seconds_amount = int(input('Type seconds amount: '))
    days = seconds_amount // 86400
    hours = (seconds_amount % 86400) // 3600
    minutes = ((seconds_amount % 86400) % 3600) // 60
    seconds = ((seconds_amount % 86400) % 3600) % 60
    print('It equals {:02d} days : {:02d} hours : {:02d} minutes : {:02d} seconds'.format(days, hours, minutes, seconds))"""

"""import random
Ball = []
for Nr in range(1,50):
    Ball.append(0)
Case = random.randint(1, 49)
for Nr in range(6):
    while Ball[Case]:
        Case = random.randint(1, 49)
    Ball[Case] = True
    print('Nr ' + str(Nr + 1) + ' => ' + str(Case))"""

"""price = 3.64
discount = 0.6
discount_price = price * (1 - discount)
breads = int(input('Type how much day old breads do you have: '))
print(' bread price: %.2f\n discount price: %.2f\n your order: %.2f' % (price, discount_price, \
                                                                    breads * discount_price))"""
'''figures = ['triangle', 'quadrangle', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']
while True:
    sides_amount = int(input('Enter sides amount of your figure: ')) - 3
    if sides_amount >= 0 and sides_amount <= (len(figures) - 1) and figures[sides_amount]:
        print('It is ' + figures[sides_amount])
    else:
        print('Wrong number. Should be from 3 to 10.')'''

'''monthes_31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
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
        print('Wrong input')'''


'''noise = {40:'room', 70:'alarm clock', 106:'mower', 130:'hammer'}
values = list(noise.keys())
sources = list(noise.values())
while True:
    noise_level = int(input('Enter noise level in decibels: '))
    if noise_level < min(values) or noise_level > max(values):
        print('Wrong input. Enter values between %.d and %.d' % (min(values), max(values)))
    else:
        for c in range(len(values)):
            if noise_level == values[c]:
                print('It is exact like ' + sources[c])
            else:
                if noise_level > values[c] and noise_level < values[c+1]:
                    print('It is between ' + sources[c] + ' and ' + sources[c+1])'''


"""while True:
    a, b, c = map(float, input('Enter length of each triangle side using SPACE between them: ').split())
    if a == b == c:
        print('equilateral')
    elif a == b or a == c or b == c:
        print('isosceles')
    else:
        print('scalene')"""

'''notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
frequences = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
name = input('Type note: ')
note = name[0]
octave = int(name[1])
octaves = [n for n in range(0, 8)]
frequence = 0
if note not in notes or octave not in octaves:
    print('Wrong input')
else:
    for c in range (len(notes)):
        if note == notes[c]:
            frequence = frequences[c] / 2 ** (4 - octave)
print(frequence)'''


"""notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
frequences = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
limit = 1
C4, D4, E4, F4, G4, A4, B4 = map(float, frequences)
while True:
    frequence = float(input('Type frequence of your note: '))
    if frequence >= C4-limit and frequence <= C4+limit:
        note = 'near C4'
    elif frequence >= D4-limit and frequence <= D4+limit:
        note = 'near D4'
    elif frequence >= E4-limit and frequence <= E4+limit:
        note = 'near E4'
    elif frequence >= F4-limit and frequence <= F4+limit:
        note = 'near F4'
    elif frequence >= G4-limit and frequence <= G4+limit:
        note = 'near G4'
    elif frequence >= A4-limit and frequence <= A4+limit:
        note = 'near A4'
    elif frequence >= B4-limit and frequence <= B4+limit:
        note = 'near B4'
    else:
        note = 'out of defined notes'
    print('This frequence is ' + note)"""

'''individuals = ['George Washington', 'Thomas Jefferson', 'Abraham Lincoln', 'Alexander Hamilton', 'Andrew Jackson', 'Ulysses s. Grant', 'Benjamin Franklin']
nominals = [1, 2, 5, 10, 20, 50, 100]

while True:
    nominal = int(input('Type the amount of banknote to check its individual: '))
    if nominal not in nominals:
        print('Such note doesn\'t exist')
    else:
        for c in range (len(nominals)):
            if nominal == nominals[c]:
                print('That is a banknote with %s on it.' % (individuals[c]))'''

'''days = [1, 1, 25]
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
        print('This date does not correspond to fixed-day holidays.')'''

"""letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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
            colour = 'black'
        else:
            colour = 'white'
        print('Field %s%d is %s.' % (letter, number, colour))"""
"""while True:
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
    print('%s is associated with this date' % (season))"""


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
