def citire_sir():
    sir = input("Introduceti un sir de caractere: ")
    return sir

def citire_matrice():
    matrice = []
    n = int(input("Introduceti numarul de randuri: "))
    m = int(input("Introduceti numarul de coloane: "))
    for i in range(n):
        rand = []
        for j in range(m):
            element = input("Introduceti elementul [{i}][{j}]: ")
            rand.append(element)
        matrice.append(rand)
    return matrice

def afisare_sir(sir):
    print("Sirul introdus este:", sir)

def afisare_matrice(matrice):
    print("Matricea introdusa este:")
    for rand in matrice:
        print(rand)

def citire_sir_fisier():
    nume_fisier = input("Introduceti numele fisierului: ")
    try:
        with open(nume_fisier, "r") as f:
            sir_fisier = f.read()
            print("Sirul citit din fisier este:", sir_fisier)
    except FileNotFoundError:
        print("Fisierul nu exista!")

if __name__ == "__main__":
    sir = citire_sir()
    matrice = citire_matrice()
    afisare_sir(sir)
    afisare_matrice(matrice)
    citire_sir_fisier()

    