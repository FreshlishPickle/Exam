zahlen = [10, 20, 30, 40, 50]

while True:
    try:
        index = int(input("Gib einen Index ein (0-4): "))
        print("Die Zahl am Index", index, "ist", zahlen[index])
        break  # Beende die Schleife, wenn die Eingabe korrekt ist
    except IndexError:
        print("Fehler: Der Index liegt außerhalb des gültigen Bereichs! Bitte versuche es erneut.")
    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl ein!")


