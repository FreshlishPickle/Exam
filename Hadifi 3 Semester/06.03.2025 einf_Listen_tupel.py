meine _liste = [1, 2, 3, 4, 5,]
print(meine_liste)

print(meine_liste[0]) #Gibt das erste Element aus: 1

meine_liste [0] =10 #Ändert das erste Element
laenge = len(meine_liste) #speichert die Länge der Liste in einer variable
meine_liste.append(6) #Fügt den Wert 6 ans Ende der Liste hinzu
meine_liste.remove(4) #Entfernt das erste Element der liste mit dem Wert 4
meine_liste.pop(2) #Entfernt das Element mit dem Index 2
del meine_liste[2] #Entfernt ebenso das Element mit dem Index 2
del  meine_liste [2:5] #Entfernt die Elemente mit dem Index von 2 bis 4

################################

mein_tupel = (1, 2, 3, 4, 5)
print(mein_tupel)

laenge2 = len(mein_tupel) #speichert die Länge das Tupel in einer Variable
print(mein_tupel[2]) #Gibt das dritte Element aus: 3

#mein_tupel[0] = 10 # Dies würde einen Fehler verursachen, weil Tupel unveränderlich sind
#wir benutzen tupel wenn wir genau wissen wie viel fest haben (z.B Wochentage), wenn wir nicht
#genau wissen dann nutzen wir liste.

#############################

meine_liste2 = list(mein_tupel)
meine_liste2.append(5)
mein_tupel2 = tuple(meine_liste2)