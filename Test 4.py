def bmi(gewicht, groesse):
    return gewicht / (groesse**2)

# Beispiel: Funktion testen
gewicht = float(input("Gib dem Gewicht in kg ein: "))
groesse = float(input("Gib der Größe in meter ein: "))
bmiWert = bmi(gewicht, groesse)
print(f"Dein BMI ist {bmiWert:.2f}")
