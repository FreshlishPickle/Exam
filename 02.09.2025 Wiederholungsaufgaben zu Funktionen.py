import math

#Aufgabe 1:

# Funktion zur Umrechnung von Celsius in Fahrenheit
def celsius_in_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

#Funktion testen
temp_celsius = float(input("Gib Temperatur in Celsius ein: "))
temp_fahrenheit = celsius_in_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C ist45 {temp_fahrenheit}°F")

#Aufgabe 2:

# Funktion zur Berechnung der Kreisfläche
def Kreisflaeche_berechnen(radius):
    flaeche = math.pi * radius**2
    return flaeche

#Funktion testen
radius = float(input("Gib den Radius des Kreises ein: "))
flaeche = Kreisflaeche_berechnen(radius)
print(f"Die Fläche des Kreises mit Radius {radius} ist {flaeche:.2f}")

#Aufgabe 3:

# Funktion zur Berechnung des Zylindervolumens
def berechne_zylindervolumen(radius, hoehe):
    volumen = math.pi * radius**2 * hoehe
    return volumen

#Funktion testen
radius = float(input("Gib den Radius des Zylinders ein: "))
hoehe = float(input("Gib die Höhe des Zylinders ein: "))
volumen = berechne_zylindervolumen(radius, hoehe)
print(f"Das Volumen des Zylinders beträgt {volumen:.2f}")

#Aufgabe 4:

# Funktion zur Umrechnung von Stunden in Sekunden
def stunden_in_sekunden(anzahlstunden):
    sekunden = anzahlstunden * 60 * 60
    return sekunden

#Funktion testen
stunden = float(input("Gib die Anzahl der Stunden ein: "))
sekunden = stunden_in_sekunden(stunden)
print(f"{stunden} Stunden entsprechen {sekunden} Sekunden")

#Aufgabe 5:

# Funktion zur Prüfung, ob ein Jahr ein Schaltjahr ist
def schaltjahr(jahreszahl):
    return (jahreszahl % 4 == 0 and jahreszahl % 100 != 0) or (jahreszahl % 400 == 0)

#Funktion testen
jahr = int(input("Gib eine Jahreszahl ein: "))
if schaltjahr(jahr):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")

#Aufgabe 6:
# Funktion zur Zählung der Vokale
def anzahl_vokale(text):
    text = text.lower()  # Alles klein schreiben, damit A/a gleich behandelt wird
    vokale = "aeiou"
    count = sum(1 for buchstabe in text if buchstabe in vokale)
    return count

#Funktion testen
eingabe_text = input("Gib einen Text ein: ")
vokale_anzahl = anzahl_vokale(eingabe_text)
print(f"Der Text enthält {vokale_anzahl} Vokale.")

#Aufgabe 7:
# Funktion zur Berechnung des Durchschnitts
def durchschnitt(zahlen):
    if len(zahlen) == 0:
        return 0  # Vermeidung von Division durch 0
    return sum(zahlen) / len(zahlen)

#Funktion testen
liste = [5, 15, 25, 35, 45]  # beliebige Zahlen
mittelwert = durchschnitt(liste)
print(f"Der Durchschnitt der Zahlen {liste} beträgt {mittelwert}")

#Aufgabe 8:

# Funktion zur Ermittlung der größten Zahl
def groesste_zahl(liste):
    if not liste:
        return None  # Wenn die Liste leer ist, gibt None zurück
    return max(liste)

#Funktion testen
zahlen = [14, 35, 5, 76, 27]
groesste = groesste_zahl(zahlen)
print(f"Die größte Zahl in {zahlen} ist {groesste}")

#Aufgabe 9:
# Funktion zur Ermittlung der kleinsten Zahl
def kleinste_zahl(liste):
    if not liste:
        return None  # Wenn die Liste leer ist, gibt None zurück
    return min(liste)

#Funktion testen
zahlen = [9, 18, 3, 52, 100]
kleinste = kleinste_zahl(zahlen)
print(f"Die kleinste Zahl in {zahlen} ist {kleinste}")

#Aufgabe 10:

# Funktion zur Berechnung des BMI
def bmi(gewicht, groesse):
    return gewicht / (groesse**2)

#Funktion testen
gewicht = float(input("Gib dem Gewicht in kg ein: "))
groesse = float(input("Gib der Größe in meter ein: "))
bmiWert = bmi(gewicht, groesse)
print(f"Dein BMI ist {bmiWert:.2f}")

#Aufgabe 11:
# Funktion zur Berechnung der Zinseszinsen
def zinseszinsen(kapital, zinssatz, jahre):
    return kapital * (1 + zinssatz/100)**jahre

#Funktion testen
startkapital = float(input("Gib das Startkapital ein: "))
zinssatz = float(input("Gib den Zinssatz in % ein: "))
laufzeit = int(input("Gib die Laufzeit in Jahren ein: "))

endkapital = zinseszinsen(startkapital, zinssatz, laufzeit)
print(f"Nach {laufzeit} Jahren beträgt das Kapital {endkapital:.2f}")















