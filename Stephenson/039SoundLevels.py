"""The following table lists the sound level in decibels for several common noises.
Noise           Decibel level (dB)

Jackhammer      130
Gas lawnmower   106
Alarm clock     70
Quiet room      40

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table."""

noise = {40:'room', 70:'alarm clock', 106:'mower', 130:'hammer'}
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
                    print('It is between ' + sources[c] + ' and ' + sources[c+1])