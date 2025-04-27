# Zadatak
# Napisati program koji ucitava N brojeva koje smesta u niz i NA KRAJU programa ih stampa.
# Potrebne su dve petlje, u jednom se desava ucitavanje niza a u drugoj stampanje.
# Primer:
# Unesite N: 10
# Unesite broj: 1
# Unesite broj: 2
# Unesite broj: 3
# Unesite broj: 4
# Unesite broj: 8
# Unesite broj: 9
# Unesite broj: 2
# Unesite broj: 1
# Unesite broj: 7
# Unesite broj: 5
# Niz je:
# 1, 2, 3, 4, 8, 9, 2, 1, 7, 5

n = int(input("Unesite broj N: "))
niz = []
for i in range(n):
    a = int(input("Unesite broj: "))
    niz.append(a)

for i in niz:
    print(i, end=", ")
