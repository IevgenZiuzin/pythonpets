"""In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units."""

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
        print('error')