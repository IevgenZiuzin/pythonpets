"""In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves."""

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
frequences = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
limit = 1
C4, D4, E4, F4, G4, A4, B4 = map(float, frequences)
while True:
    frequence = float(input('Type frequence of your note: '))
    if C4-limit <= frequence <= C4+limit:
        note = 'near C4'
    elif D4-limit <= frequence <= D4+limit:
        note = 'near D4'
    elif E4-limit <= frequence <= E4+limit:
        note = 'near E4'
    elif F4-limit <= frequence <= F4+limit:
        note = 'near F4'
    elif G4-limit <= frequence <= G4+limit:
        note = 'near G4'
    elif A4-limit <= frequence <= A4+limit:
        note = 'near A4'
    elif B4-limit <= frequence <= B4+limit:
        note = 'near B4'
    else:
        note = 'out of defined notes'
    print('This frequence is ' + note)