alleZahlen = []
geradeZahlen = []
ungeradeZahlen = []

for zahl in range(1,100):
    alleZahlen.append(zahl)

    if zahl %2 ==0:
        geradeZahlen.append(zahl)

    else:
        ungeradeZahlen.append(zahl)


print("Alle Zahlen:", alleZahlen)
print("Alle geraden Zahlen:", geradeZahlen)
print("Alle ungeraden Zahlen:", ungeradeZahlen)