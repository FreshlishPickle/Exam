try:
    unseralter = int(input("Gib dein Alter ein:"))
    print(f"wir sind {unseralter} Jahre alt")
except ValueError:
    print("DU kannst nur Zahlen eingeben")

