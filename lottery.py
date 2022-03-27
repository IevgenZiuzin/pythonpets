import random
Ball = []
for Nr in range(1,50):
    Ball.append(0)
Case = random.randint(1, 49)
for Nr in range(6):
    while Ball[Case]:
        Case = random.randint(1, 49)
    Ball[Case] = True
    print('Nr ' + str(Nr + 1) + ' => ' + str(Case))