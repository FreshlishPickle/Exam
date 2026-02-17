werte = []
with open("tesla_schlusskurse_2025_komma.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:  # Leere Zeilen überspringen
            teile = line.split()           # Zeile nach Leerzeichen trennen
            kurs_str = teile[1]           # letzter Teil ist der Kurs
            kurs = float(kurs_str.replace(",", "."))
            werte.append(kurs)

# Erste 10 Werte zur Kontrolle
print("Erste 10 Werte:", werte[:10])
