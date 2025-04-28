import math

def eingabe_option():
    while True:
        print("---------------------------")
        print("0. Beenden")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Quadratwurzel")
        print("6. Exponentialberechnung")
        print("---------------------------")
        try:
            return int(input("Bitte wähle eins der Optionen: "))
        except ValueError:
            print("Bitte gib eine Option ein.")

def eingabe_nummer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Bitte gib eine Nummer ein.")

while True:
    ergebnis = 0
    option = eingabe_option()
    if option == 0:
        break
    elif option == 1:
        a = eingabe_nummer("Gib die erste Nummer ein: ")
        b = eingabe_nummer("Gib die zweite Nummer ein: ")
        ergebnis = a + b
    elif option == 2:
        a = eingabe_nummer("Gib die erste Nummer ein: ")
        b = eingabe_nummer("Gib die zweite Nummer ein: ")
        ergebnis = a - b
    elif option == 3:
        a = eingabe_nummer("Gib die erste Nummer ein: ")
        b = eingabe_nummer("Gib die zweite Nummer ein: ")
        ergebnis = a * b
    elif option == 4:
        a = eingabe_nummer("Gib die erste Nummer ein: ")
        b = eingabe_nummer("Gib die zweite Nummer ein: ")
        ergebnis = a / b
    elif option == 5:
        a = eingabe_nummer("Gib eine Nummer ein: ")
        ergebnis = math.sqrt(a)
    elif option == 6:
        a = eingabe_nummer("Gib eine Nummer ein: ")
        b = eingabe_nummer("Gib eine Nummer ein: ")
        ergebnis = a ** b

    if option != 0:
        print("Ergebnis ist " + str(ergebnis))
