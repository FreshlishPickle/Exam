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


f = open("Dateien_Teil_B_C\\tesla_schlusskurse_2025_fehler1.txt","r")




d,p = ReadDataFromFile(f," ")
print(d)
print(p)