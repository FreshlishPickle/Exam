# Dateiname
datei_name = "aufgabe10.txt"

# Aktuelle Namen aus der Datei lesen
vorhandene_namen = set()
with open(datei_name, 'r', encoding='utf-8') as datei:
    for zeile in datei:
        name = zeile.strip()
        if name:  # Nur nicht-leere Zeilen berücksichtigen
            vorhandene_namen.add(name)

# Neuen Namen vom Benutzer abfragen
neuer_name = input("Bitte geben Sie einen Namen ein: ").strip()

# Prüfen, ob der Name bereits vorhanden ist
if neuer_name in vorhandene_namen:
    print("Schon vorhanden")
else:
    # Name an die Datei anhängen
    with open(datei_name, 'a', encoding='utf-8') as datei:
        datei.write(f"\n{neuer_name}")
    print(f"Der Name '{neuer_name}' wurde hinzugefügt.")

