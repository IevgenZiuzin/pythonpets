"""A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user."""

price = 3.64
discount = 0.6
discount_price = price * (1 - discount)
breads = int(input('Type how much day old breads do you have: '))
print(' bread price: %.2f\n discount price: %.2f\n your order: %.2f' % (price, discount_price, \
                                                                    breads * discount_price))