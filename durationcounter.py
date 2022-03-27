while True:
    tacts = int(input('Set tacts: '))
    bpm = int(input('Set bpm: '))
    def convert_tacts_to_duration(tacts, bpm):
        beats_per_tact = 4
        tact_per_minute = bpm / beats_per_tact
        tact_duration_seconds = 60 / tact_per_minute
        duration = tacts * tact_duration_seconds
        return duration
    total_seconds = convert_tacts_to_duration(tacts, bpm)
    print('\nDuration: ' + str(int(total_seconds / 60)) + ':' + str(int(total_seconds % 60)) + '\n')
    cont = input('One more time? (y/n) ')
    if cont == 'n':
        break

