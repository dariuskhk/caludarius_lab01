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

if __name__ == "__main__":
    sir= citire_sir()
    matrice = citire_matrice()
    afisare_sir(sir)
    afisare_matrice(matrice)

