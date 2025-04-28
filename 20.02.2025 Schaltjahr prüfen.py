# Eingabe eines Jahres vom Benutzer

jahr = int(input("Gib ein Jahr ein: "))

# Überprüfung, ob es ein Schaltjahr ist

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print(f"{jahr} ist ein Schaltjahr.")

else:
    print(f"{jahr} ist kein Schaltjahr.")


    
