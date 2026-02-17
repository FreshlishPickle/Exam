#-------- Aufgabe 2 ----------

def max_wert(liste):
    if not liste:
        return None     # wenn Liste leer ist None zurückgeben

    maximum = liste[0]   # Am start: wir nehmen das erste Element als größte
    for zahl in liste:    # Alle Zahlen in der Liste durchlaufen
        if zahl > maximum:
            maximum = zahl
    return maximum   # am Ende: größtes Element zurückgeben

zahlen = [6, 8, 9, 91, 100]
print(max(zahlen))

#-------- Aufgabe 2 ----------

def filter_gerade(liste):

    gerade=[] # Leere Liste für die gerade Zahlen
    for zahl in liste:
        if zahl % 2 == 0:  # Gerade Zahlen haben ein Rest von 0, wenn Dividiert.
            gerade.append(zahl) # Zahlen in ergebnisliste einfügen
    return gerade

print(filter_gerade([2, 7, 8, 99, 80]))

#-------- Aufgabe 3 ----------

def element_häufigkeit(liste):
    häufigkeit ={}  #Wörterbuch für Elemente und deren Anzahl
    for element in liste:
        if element in häufigkeit:
            häufigkeit[element] += 1 # Zähler um 1 erhöhen
        else:
             häufigkeit[element] = 1  #Element zum ersten Mal auf 1 setzen
    for elem,count in häufigkeit.items(): # Ausgabe aller Elemente mit deren Anzahl
        print(f"{elem}: {count}")

element_häufigkeit(["Apfel", "Banana", "Apfel", "Banana", "Erdbeeren", "Ananas", "Erdbeeren"])

#-------- Aufgabe 4 ----------

namen = []  # Liste für Schülernamen
noten = []  # Liste für die Noten (Parallel zu namen)

def note_hinzufügen(namen, noten, schülername, note):
    namen.append(schülername) #Name an Liste anhängen
    noten.append(note) # Note an Liste anhängen

def durchschnittsnote(noten):
    if not noten:   # falls keine Note vorhanden ist
        return 0
    return sum(noten) / len(noten) # Summe geteilt durch Noten Anzahl

def beste_note(namen, noten):
    if not noten:
        return None
    beste_index = 0  # Erste Note ist die Beste
    for i in range(len(noten)):
        if noten[i] < noten[beste_index]:  # kleinere Note = besser
            beste_index = i
    return namen[beste_index] # Schülername mit bester Note geben

note_hinzufügen(namen, noten, "Hidar", 1.1)
note_hinzufügen(namen, noten, "Leon", 3.0)
note_hinzufügen(namen, noten, "Karim", 1.3)

print(durchschnittsnote(noten))
print(beste_note(namen, noten))

#-------- Aufgabe 5 ----------

'''Ein Dictionary ist ein Datenstruktur auf Python, mit dem man Werte über Schlüssel (Key) speichert und abruft '''

wechselkurse = {
    "EUR_to_USD": 1.1,
    "USD_to_EUR": 0.91,     # Dictionary mit festen Wechselwerte
    "EUR_to_GBP": 0.85,
    "GBP_to_EUR": 1.18,
    "USD_to_GBP": 0.77,
    "GBP_to_USD": 1.3
}

def währungsumrechnung(betrag, wechselkurs):
    return betrag * wechselkurs

def waehrung_waehlen(betrag, von, nach):
    key = f"{von}_to_{nach}"            #Schlüssel in Dictionary erstellen
    if key in wechselkurse:      # Prüfen, ob kurs existiert
        return währungsumrechnung(betrag, wechselkurse[key])
    else:
        return "Wechselkurs ist nicht verfügbar."

print(waehrung_waehlen(3975, "EUR", "USD"))
print(waehrung_waehlen(9750, "USD", "GBP"))
print(waehrung_waehlen(1760, "GBP", "EUR"))













