# Zadatak
# Napisati program koji ucitava niz A duzine N, i koji nakon unosa niz A stampa sve elemente niza koji su veci od nule.
# Primer izvrsenja:
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: -4
# Unesite broj: 3
# Unesite broj: -7
# Unesite broj: 9

# Brojevi veci od nule u nizu A su: 1, 3, 9,

n = int(input("Unesite broj N: "))
niz_a = [int(input("Unesite broj: ")) for _ in range(n)]

print("Brojevi veci od nule su nizu A su: ", end="")
for value in niz_a:
    if value > 0:
        print(f"{value}", end=", ")
