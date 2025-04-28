# wir nutzen try .. except falls der Benutzer eine ungültige Eingabe macht
# damit eine Fehler Meldung kommt

try:
    start = int(input("Geben Sie die erste ganze Zahl ein: "))
    ende = int(input("Geben Sie die zweite ganze Zahl ein: "))

    # wir stellen sicher dass start <= ende

    if start > ende:
        start, ende = ende, start

    # wir geben die Zahlenreihe
    zahlenreihe = list(range(start, ende +1))
    print("Zahlenreihe: ", str(zahlenreihe))

except ValueError:
    print("Fehler: Bitte geben Sie eine gueltige ganze zahl ein ")

