import random
import string
adjectives = ['exact', 'successive', 'adjacent', 'certain', 'similar', 'rare', 'true', 'receptive', 'accessible', 'availeble']
nouns = ['ambit', 'settlement', 'reference', 'effect', 'framework', 'cutting', 'end', 'influence', 'route', 'conquest']

print('\n GENERATE NEW PASSWORD \n')
input('Press Enter to continue')
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,50)
    character = random.choice(string.punctuation)
    password = adjective + noun + str(number) + character
    print(' \n Your password: ' + password + '\n')
    response = input('Another one? (y/n): ')
    if response == 'n':
        break
