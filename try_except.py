#Beim Programmieren können Fehler auftreten, z. B.:

#Falsche Eingaben (z. B. Buchstaben statt Zahlen)
#Mathematische Fehler (z. B. Division durch null)
#Dateifehler (z. B. Datei nicht gefunden)

# Wieso ist ein Fehlerabfang mit try-except wichtig?
# Geben wir in folgendem Programm bspw. einen Buchstaben ein, bricht das Programm vollständig ab,
#   da wir einen Integer Wert eingeben wollen.
alter = int(input("Gib dein Alter ein:"))
if alter >= 18:
    print("Volljährig!")
else:
    print("Minderjährig")

# Wir haben zuvor schon gelernt, dass ohne int() um den input alle Eingaben ein String sind
#   -> Der Wert kann nicht mit der Zahl 18 verglichen werden
'''
alter = input("Gib dein Alter ein:")
if alter >= 18:
    print("Volljährig!")
else:
    print("Minderjährig")
'''

# Ein erstes Beispiel:
try:
    # Code, der möglicherweise einen Fehler verursacht
    zahl = int(input("Gib eine Zahl ein: "))
    print("Deine Zahl:", zahl)
except ValueError:
    # Code, der ausgeführt wird, wenn ein Fehler auftritt
    print("Fehler: Bitte eine gültige Zahl eingeben!")

# Ein Beispiel mit mehreren Fehlerabfängen
try:
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))
    ergebnis = zahl1 / zahl2
    print("Ergebnis:", ergebnis)
except ValueError:
    print("Fehler: Bitte nur Zahlen eingeben!")
except ZeroDivisionError:
    print("Fehler: Division durch Null nicht erlaubt!")


# Allgemeiner Fehlerabfang, wenn man noch nicht weiß welcher Fehler auftreten kann
# Nicht optimal, besser konkreten Fehlerabfang nutzen
try:
    x = int(input("Gib eine Zahl ein: "))
    y = 10 / x
except Exception as e:
    print("Es ist ein Fehler aufgetreten:", e)


# try-except + else / finally
try:
    zahl = int(input("Gib eine Zahl ein: "))  # Versuch, eine Zahl einzugeben
    print("Deine Zahl:", zahl)
except ValueError:
    print("Fehler: Bitte eine gültige Zahl eingeben!")  # Falls die Eingabe fehlschlägt
else:
    print("Eingabe war erfolgreich!")  # Falls kein Fehler passiert
finally:
    print("Programm wird beendet.")  # Wird immer ausgeführt (egal ob Fehler oder nicht)
# Wenn eine 5 eingegeben wrd, dann wird der else- und finally-Block ausgeführt
# Wenn ein U eingegeben wird, dann wird der except- und finally-Block ausgeführt

# else ist praktisch, wenn du nach einer erfolgreichen try-Ausführung noch etwas tun willst.
# finally ist nützlich, wenn du sicherstellen musst, dass bestimmte Dinge immer passieren (z. B. Datei schließen).
# (Mit Dateien arbeiten wird bald)


# try-except + raise
try:
    temperatur = float(input("Gib eine Temperatur in Celsius ein: ")) # Der Benutzer gibt eine Temperatur ein.

    #Falls die Eingabe kleiner als -273.15 (der absolute Nullpunkt) ist, wird eine eigene ValueError-Exception ausgelöst.
    if temperatur < -273.15:
        raise ValueError("Fehler: Die Temperatur kann nicht unter -273,15 °C liegen (absoluter Nullpunkt).")

    print(f"Die eingegebene Temperatur beträgt {temperatur}°C.")
# Falls ein Fehler auftritt (z. B. falsche Eingabe oder zu niedrige Temperatur),
# fängt der except-Block diesen ab und gibt eine entsprechende Meldung aus.
except ValueError:
    print("Fehler:", ValueError)