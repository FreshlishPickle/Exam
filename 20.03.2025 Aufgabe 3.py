def berechne_eintrittspreis():



        try:
            alter = int(input("Bitte geben Sie Ihr Alter ein: "))

            if alter < 0 or alter > 120:
                print("Fehler: Bitte geben Sie ein realistisches Alter zwischen 0 und 120 ein.")
            else:
                if alter < 12:
                    preis = 5
                elif alter <= 65:
                    preis = 20
                else:
                    preis = 10

                print(f"Der Eintrittspreis beträgt {preis} Euro.")
        except ValueError:
            print("Fehler: Bitte geben Sie eine gültige Zahl ein.")


berechne_eintrittspreis()
