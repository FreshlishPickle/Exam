def geld_abheben():
    kontostand = 500

    try:
        betrag = float(input("Geben Sie den Betrag ein, den Sie abheben möchten: "))

        if betrag <= 0:
            print("Fehler: Der Betrag muss positiv sein.")
        elif betrag > kontostand:
            print("Fehler: Nicht genügend Guthaben auf dem Konto.")
        else:
            kontostand -= betrag
            print(f"Abhebung erfolgreich. Neuer Kontostand: {kontostand:.2f} Euro")

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Zahl ein.")



geld_abheben()