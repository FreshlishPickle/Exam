def note_berechnen(punkte):
    if punkte < 30:
        return  6
    elif punkte < 50:
        return 5
    elif punkte < 67:
        return 4
    elif punkte < 82:
        return 3
    elif punkte < 92:
        return 2
    else:
        return 1
print("Für 100 Punkte bekommst du eine " + str(note_berechnen(100)))
