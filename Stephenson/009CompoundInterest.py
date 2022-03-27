"""Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places."""

deposit = float(input('Type your deposite: '))
yearly_rate = float(input('Type percent interest per year: '))
years_number = int(input('Type number of years: '))
current_year = int(input('Type current year: '))
for c in range(current_year + 1, current_year + years_number):
      yearly_earn = deposit * (yearly_rate/100)
      deposit = yearly_earn + deposit
      print(str(c) + (': %.2f' % (deposit)))