zahlen = [10, 20, 30, 40, 50]

try:
    index = int(input("Gib einen Index ein (0-4): "))
    print("Die Zahl am Index", index, "ist", zahlen[index])
except IndexError:
    print("Fehler: Der Index liegt außerhalb des gültigen Bereichs!")
except ValueError:
    print("Fehler: Bitte gib eine gültige Zahl ein!")

