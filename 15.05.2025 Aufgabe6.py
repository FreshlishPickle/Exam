# Dateiname
datei_name = "aufgabe06.txt"

# Drei neue Wörter vom Benutzer einlesen
print("Bitte geben Sie drei neue Wörter ein:")
wort1 = input("1. Wort: ")
wort2 = input("2. Wort: ")
wort3 = input("3. Wort: ")

# Wörter an die Datei anhängen
with open(datei_name, 'a', encoding='utf-8') as datei:
    datei.write(f"\n{wort1}\n{wort2}\n{wort3}\n")

print("Die drei neuen Wörter wurden erfolgreich an die Datei angehängt.")