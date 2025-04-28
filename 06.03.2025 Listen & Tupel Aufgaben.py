#Aufgabe 1

#1-Liste gegeben
meine_liste = [1, 2, 3, 4, 5]
print(meine_liste)
#2-Dritte Element auf 10 geändert
meine_liste[2] = 10
print(meine_liste)
#3-Zahl 6 am Ende Fügen
meine_liste.append(6)
print(meine_liste)
#4-Die Zahl 4 würde entfernt
meine_liste.remove(4)
print(meine_liste)
#5-modifizierte Liste ausgegeben
print(meine_liste)


#Aufgabe2

#1-Tupel Erstellen und 2- ausgegeben
mein_tupel = (1, 2, 3)
print(mein_tupel)
#3-Versuchen ein Element zu ändern,4- Tupel in eine Liste Wandeln
tupel_liste = list(mein_tupel)
tupel_liste.append(4)
#5-ursprüngliche Tupel ausgeben
meine_tupel= tuple(tupel_liste)
print(tupel_liste)


#Aufgabe 3

#1-Liste mit 5 zufälligen Zahlen
import random
liste =[random.randint(0, 100) for x in range(5)]
print(liste)
#2-for-schleife um alle zahlen auszugeben
for x in liste:
    print(x)
#3- while-schleife verwenden bis die Zahl 5 erreicht würde
e=0
while e <len(liste):
    print(liste[e])
    e+=1


#Aufgabe 4

#1-Liste der Noten ausgegeben
noten = [4, 5, 6, 2, 1]
print("liste der Noten", noten)
#2-Den Durchschnitt der Noten zu berechnen und auszugeben.
durschschnitt = sum(noten) / len(noten)
print("durschschnitt der Noten", durschschnitt)
#3-Die höchste und die niedrigste Note zu ermitteln.
niedrigste_Note= max(noten)
höchste_note= min(noten)
print("Niedrigste Note:", niedrigste_Note)
print("Höchste Note:", höchste_note)
#4-Noten sortieren
sortierte_noten = sorted(noten)
print("Sortierte Noten", sortierte_noten)



