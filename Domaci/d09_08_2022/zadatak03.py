# Napisati program koji ucitava niz A duzine N i broj X.
# Nakon unosa treba ispisati indekse onih clanova niza koji su jednaki broju X.
# Primer izvrsenja:
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 3
# Unesite broj: 7
# Unesite broj: 3
# Unesite broj: 9
# Unesite X: 3

# Rezultat: Elementi niza A koji su jednaki broju X imaju indekse: 1, 3

a = int(input("Unesite A: "))
niz = [int(input("Unesite broj: ")) for _ in range(a)]
x = int(input("Unesite broj X: "))

print("Rezulat: Elementi niza A koju su jednaki broju X imaju indekse: ", end="")
for i, value in enumerate(niz):
    if x == value:
        print(i, end=", ")
