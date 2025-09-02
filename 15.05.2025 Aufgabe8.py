# Dateinamen
quell_datei = "aufgabe08.txt"
ziel_datei = "sortiert.txt"

# Wörter aus der Quelldatei lesen
woerter = []
with open(quell_datei, 'r', encoding='utf-8') as datei:
    for zeile in datei:
        wort = zeile.strip()  # Leerzeichen und Zeilenumbrüche entfernen
        if wort:  # Nur nicht-leere Zeilen berücksichtigen
            woerter.append(wort)

# Wörter alphabetisch sortieren (case-insensitive)
woerter.sort(key=lambda x: x.lower())

# Sortierte Wörter in die Zieldatei schreiben
with open(ziel_datei, 'w', encoding='utf-8') as datei:
    for wort in woerter:
        datei.write(wort + "\n")

print(f"Die Wörter wurden alphabetisch sortiert und in '{ziel_datei}' gespeichert.")