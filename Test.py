# wir definieren unsere Tupel mit zufällige Zahlen
zahlen = [12, 5, 8, 21, 30, 7, 14, 3, 25, 18]

#wir definieren die Tupels in Zahlengruppen

klein = []
mittel = []
gross = []

# wir loopen durch die Zahlen
for zahl in zahlen:

    #wenn die Zahl kleiner als 10 ist, kommt in Gruppe klein
        if zahl < 10:
            klein.append(zahl)

        elif zahl > 20:
            gross.append(zahl)

        else:
            mittel.append(zahl)


#wir geben die Gruppen ein:

print("Klein: " +str(klein))
print("mittel: " + str(mittel))
print("Gross: " + str(gross))


