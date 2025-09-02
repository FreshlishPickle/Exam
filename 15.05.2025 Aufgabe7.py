# Dateiname
datei_name = "aufgabe07.txt"

# Liste für die Zahlen vorbereiten
zahlen = []

# Datei lesen und Zahlen verarbeiten
with open(datei_name, 'r', encoding='utf-8') as datei:
    for zeile in datei:
        zeile = zeile.strip()  # Einmal strip() aufrufen und Ergebnis speichern
        if zeile:  # Nur nicht-leere Zeilen verarbeiten
            try:
                zahlen.append(int(zeile))
            except ValueError:
                print(f"Warnung: '{zeile}' ist keine gültige Zahl und wird ignoriert")

# Größte Zahl finden
if zahlen:
    groesste_zahl = max(zahlen)
    print(f"Die größte Zahl in der Datei ist: {groesste_zahl}")
else:
    print("Die Datei enthält keine gültigen Zahlen.")