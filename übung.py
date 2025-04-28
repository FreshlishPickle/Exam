zahl= float (input("Gib ein Zahl ein"))

if zahl > 0:
    print("Die Zahl ist positiv")

elif zahl < 0:
    print("Die Zahl ist negative")

else:
    print("Die Zahl ist Null")





Zahl= int (input("Gib ein Zahl ein"))

if Zahl % 2 ==0:
    print("Die zahl ist gerade")

else:
    print("Die Zahl ist ungerade")





    Jahr = int (input("Gib ein Jahr ein"))

    if (Jahr % 4 == 0 and Jahr  % 100 != 0) or (Jahr %400 == 0):

        print(f"{Jahr} ist ein Schaltjahr")

    else:
        print(f"{Jahr} ist kein Schaltjahr")