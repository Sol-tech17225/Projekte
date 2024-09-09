# Funksie om 'n item by die lys te voeg
def voeg_item_by(lys, item, prys):
    lys.append((item, prys))

# Funksie om die lys van items te vertoon
def vertoon_lys(lys):
    totaal = 0
    for item, prys in lys:
        print(f"{item}   R{prys:.2f}")
        totaal += prys
    print("---------------")
    print(f"Totaal R{totaal:.2f}")

# Funksie om die lys skoon te maak
def maak_skoon(lys):
    lys.clear()

# Hoofprogram wat die POS-stelsel bestuur
def pos_stelsel():
    items = []
    while True:
        print("Kies operasie:")
        print("1. Voeg item by")
        print("2. Vertoon lys")
        print("3. Maak skoon")
        print("4. Verlaat")

        # Neem die gebruiker se keuse
        keuse = input("Voer keuse in (1/2/3/4): ")

        if keuse == '1':
            item = input("Voer item naam in: ")
            try:
                prys = float(input("Voer item prys in: "))
            except ValueError:
                print("Ongeldige invoer. Voer asseblief 'n getal in.")
                continue
            voeg_item_by(items, item, prys)
        elif keuse == '2':
            vertoon_lys(items)
        elif keuse == '3':
            maak_skoon(items)
            print("Lys is skoongemaak.")
        elif keuse == '4':
            print("Verlaat die POS-stelsel.")
            break
        else:
            print("Ongeldige keuse. Probeer asseblief weer.")

# Roep die hoofprogram aan
pos_stelsel()
