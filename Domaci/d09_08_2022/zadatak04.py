# (Za vezbanje) Napisati program koji ucitava niz a duzine N.
# Nakon unosa niza a, formira se niz b tako sto se prva 3 elementa niza a kopiraju u niz b,
# a ostale elemente niza b ispuniti jedinicama.(niz b je iste duzine kao i niz a)

# Unesite N: 6
# Unesite broj: 1
# Unesite broj: 5
# Unesite broj: 2
# Unesite broj: 7
# Unesite broj: 8
# Unesite broj: -1

# Niz a: 1, 5, 2, 7, 8, -1
# Niz b: 1, 5, 2, 1, 1, 1

n = int(input("Unesite broj N: "))
niz_a = [int(input("Unesite broj: ")) for _ in range(n)]

niz_b = []

for i in range(3):
    niz_b.append(niz_a[i])

for i in range(len(niz_a)-3):
    niz_b.append(1)

print(f"Niz a: {niz_a}")
print(f"Niz a: {niz_b}")
