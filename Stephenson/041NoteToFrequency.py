"""The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
Note Frequency (Hz)
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88
Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement."""

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
frequences = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
name = input('Type note: ')
note = name[0]
octave = int(name[1])
octaves = [n for n in range(0, 8)]
frequence = 0
if note not in notes or octave not in octaves:
    print('Wrong input')
else:
    for c in range(len(notes)):
        if note == notes[c]:
            frequence = frequences[c] / 2 ** (4 - octave)
print(frequence)