def quadrat_berechnen():
    try:
        zahl = int(input("Bitte eine Ganzzahl eingeben: "))
        print(f"Das Quadrat der Zahl ist: {zahl ** 2}")
    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Ganzzahl ein.")

quadrat_berechnen()
quadrat_berechnen()
quadrat_berechnen()
