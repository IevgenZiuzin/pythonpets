def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess == answer:
            print('\n Well done! \n Score: +1 \n')
            score = score + 1
            still_guessing = False
        else:
            if answer == 'y':
                print('Next time!')
                still_guessing = False
            elif answer == 'n':
                print('Next time!')
                still_guessing = False
            else:
                if attempt < 2:
                    guess = input('Try again - ')
            attempt = attempt + 1
    if attempt == 3:
        print(' \n So it was: \n' + answer + '\n')
score = 0
print('\n WORDS TRAINER \n')
guess0 = input('Adhere on rules (y/n): ')
check_guess(guess0, 'n')
guess00 = input('Adhere to rules (y/n): ')
check_guess(guess00, 'y')
guess1 = input('повышать, расширять, усиливать - ')
check_guess(guess1, 'increase')
guess2 = input('цена, значение, величина, оценивать - ')
check_guess(guess2, 'value')
guess3 = input('наше будущее соглашение - ')
check_guess(guess3, 'our future agreement')
guess4 = input('в вашем распоряжении - ')
check_guess(guess4, 'at your disposal')
guess5 = input('пожалуйста, напомни мне - ')
check_guess(guess5, 'please, remind me')
guess6 = input('мы расширяем наш бизнес - ')
check_guess(guess6, 'we\'re extending our business')
guess7 = input('предоставлять, обеспечивать, предусматривать - ')
check_guess(guess7, 'provide')
guess8 = input('их успех зависит от того, \n насколько хорошо они следуют правилам - ')
check_guess(guess8, 'their success depends on how well they adhere to rules')
guess9 = input('главная забота, интерес - ')
check_guess(guess9, 'the main concern')
guess10 = input('вам приятно будет узнать - ')
check_guess(guess10, 'you\'ll be pleased to hear')
print('Total Score: ' + str(score))
