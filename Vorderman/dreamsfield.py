import random
lives = 10
words = ['apart', 'exact', 'ambit', 'truly', 'value', 'limit', 'circumstances', 'cut', 'lay']
secret_word = random.choice(words)
clue = []
heart_symbol = u'\u2764'
fullguess = False
index = 0
global score
unknown_letters = len(secret_word)
def update_clue(guess, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guess == secret_word[index]:
            clue[index] = guess
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters
print('\n Lives: ' + heart_symbol * lives + '\n')
while index < len(secret_word):
    clue.append('?')
    index = index + 1
while lives > 0:
    print(clue)
    guess = input('Guess letter or word: ')
    if guess == secret_word:
        fullguess = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue, unknown_letters)
        unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        print('\n Yes! \n')        
    else:
        if len(guess) < 2:
            print('\n Wrong answer. You lost one life \n \n Lives: ' + heart_symbol * lives + '\n')
            lives = lives - 1
        else:
            lives = 0        
            print('\n Wrong answer. It was: ' + secret_word + '\n Game over. \n')
    if unknown_letters == 0:
        fullguess = True
        break
score = lives * 10
if fullguess:
    print('\n You win! Really: ' + secret_word)
print('\n Score: ' + str(score))

