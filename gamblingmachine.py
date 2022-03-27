import random
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
            machine_delay = 2