# wir definieren eine Liste mit Zahlen
zahlen = [3, 5, 1, 6, 33, 6, 9, 21]

#wir definieren die kleineste zahl ein

kleineste = min(zahlen)
groesste = max(zahlen)
anzahl = len(zahlen)
durchschnitt = sum(zahlen) / anzahl

# wir geben alles aus

print("Kleineste Zahl: " +str(kleineste))
print("Groesste Zahl: " + str(groesste))
print("Anzahl von Werten: " +str(anzahl))
print("Durchschnitt von Zahlen: " +str(durchschnitt))
