# Napisati program koji ima definisan niz od N broja i od korisnika ucitava N brojeva i cuva ih u niz.
# Nakon unosa brojeva sracunati sumu niza i prikazati je na kraju programa.
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
# Unesite broj: 70
# Unesite broj: 5
# Suma je 42

n = int(input("Unesite broj N: "))
niz = []
for i in range(n):
    a = int(input("Unesite broj: "))
    niz.append(a)

suma = 0
for i in niz:
    suma = suma + i
print(suma)
