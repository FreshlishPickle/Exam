with open("tesla_schlusskurse_2025_asr.txt","r") as f:
    tesla_stock = f.readlines()
    f.close()

print(tesla_stock)

anzahl_zeilen = 0

for zeile in tesla_stock:
    
    datum = zeile.strip().split("! !")[0]
    preis = zeile.strip().split("! !")[1]

    preis = float(preis)

    print(f"Am Datum: {datum} kostet das Tesla-Aktie PREIS: {preis.__round__(2)} USD")

    anzahl_zeilen +=1 #oder anzahl_zeilen = anzahl_zeilen +1

    if anzahl_zeilen == 3:
        break

'''Die oben geschriebene Aufgabe ist Aufgabe 1A'''

with open("tesla_schlusskurse_2025_asr.txt", "r") as f:
    tesla_stock = f.readlines()
    f.close()

datum_liste = []
preis_liste= []


print(tesla_stock)

anzahl_zeilen = 0

for zeile in tesla_stock:

    datum = zeile.strip().split("! !")[0]
    preis = zeile.strip().split("! !")[1]

    preis = float(preis)

    datum_liste.append(datum)
    preis_liste.append(preis)

    print(f"Am Datum: {datum} kostet das Tesla-Aktie PREIS: {preis.__round__(2)} USD")

    anzahl_zeilen += 1  # oder anzahl_zeilen = anzahl_zeilen +1

    if anzahl_zeilen == 10:
        break

'''Die oben geschriebene Aufgabe ist Aufgabe 1B'''

def ReadDataFromFile(file_pointer, trennzeichen):
    datum_liste = []
    preis_liste = []

    tesla_stock = file_pointer.readlines()
    print(tesla_stock)

    anzahl_zeilen = 0

    for zeile in tesla_stock:
        datum = zeile.strip().split(trennzeichen)[0]
        preis = zeile.strip().split(trennzeichen)[1]
        preis = float(preis)

        datum_liste.append(datum)
        preis_liste.append(preis)

        print(f"Am Datum: {datum} kostet das Tesla-Aktie PREIS: {preis.__round__(2)} USD")

        anzahl_zeilen += 1
        if anzahl_zeilen == 10:
            break

    return datum_liste, preis_liste

