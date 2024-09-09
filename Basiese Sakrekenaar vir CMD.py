# Funksie om twee getalle op te tel
def add(x, y):
    return x + y

# Funksie om twee getalle af te trek
def subtract(x, y):
    return x - y

# Funksie om twee getalle te vermenigvuldig
def multiply(x, y):
    return x * y

# Funksie om twee getalle te deel
def divide(x, y):
    return x / y

# Hoofprogram wat die sakrekenaar bestuur
def calculator():
    while True:
        print("Kies operasie:")
        print("1. Plus (+)")
        print("2. Minus (-)")
        print("3. Maal (*)")
        print("4. Deel (/)")
        print("5. Verlaat")

        # Neem die gebruiker se keuse
        choice = input("Voer keuse in (1/2/3/4/5): ")

        # Kontroleer of die keuse geldig is
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Voer eerste getal in: "))
                num2 = float(input("Voer tweede getal in: "))
            except ValueError:
                print("Ongeldige invoer. Voer asseblief 'n getal in.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                else:
                    print("Kan nie deur nul deel nie.")
        elif choice == '5':
            print("Verlaat die sakrekenaar.")
            break
        else:
            print("Ongeldige keuse. Probeer asseblief weer.")

# Roep die hoofprogram aan
calculator()
