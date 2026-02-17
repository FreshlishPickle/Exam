zahl = float(input("Bitte geben Sie Ihre Zahl ein: "))


print("Ihre eingegebene Zahl lauter:",zahl)

print(f"Ihre eingegebene Zahl lauter:{zahl}")

print(f"Ihre eingegebene Zahl lautet: {zahl:.2f}")

if zahl < 10:

    print("zu klein")

elif zahl >= 100:

    print("zu groß")

else:

    print("Klappt")


# funktion soll ausgeben ob es zu war, zu kalt oder genau richtig ist
#kleiner 20: kalt
#groöer gleich 20 und kleiner gleich 40: ok
#größer 40: zu warm



def temperatur(temp):
    if temp < 20:
        print("Zu kalt")
    elif 20 <= temp <= 40:
        print("Genau richtig")
    else:
        print("Zu warm")

#20mal nach Temperatur gefragt
for x in range(0,20):
    eingabe = int(input("Bitte geben Sie Ihre Temperatur ein: "))
    temperatur(eingabe)







