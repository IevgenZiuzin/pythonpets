"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places."""

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
        print('error')