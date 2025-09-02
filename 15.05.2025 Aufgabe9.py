# Dateinamen
datei1 = "aufgabe09_1.txt"
datei2 = "aufgabe09_2.txt"
ziel_datei = "gesamt.txt"

# Inhalt beider Dateien lesen und kombinieren
with open(datei1, 'r', encoding='utf-8') as f1, \
        open(datei2, 'r', encoding='utf-8') as f2, \
        open(ziel_datei, 'w', encoding='utf-8') as ziel:
    # Inhalt der ersten Datei schreiben
    ziel.write(f1.read())

    # Optional: Leerzeile zwischen den Inhalten einfügen
    ziel.write("\n")

    # Inhalt der zweiten Datei schreiben
    ziel.write(f2.read())

print(f"Die Inhalte wurden erfolgreich in '{ziel_datei}' zusammengeführt.")