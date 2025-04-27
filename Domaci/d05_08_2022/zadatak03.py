# Napisati program koji od korisnika ucitava N brojeva i sabira samo parne brojeve.
# Na kraju programa prikazati sumu.
# Primer izvrsenja:
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 2
# Unesite broj: 9
# Unesite broj: 6
# Unesite broj: 8
# Suma parnih brojeva je 16
# Objasnjenje: 2 + 6 + 8 = 16

suma = 0
n = int(input("Unesite N: "))

for i in range(n):
    a = int(input("Unesite broj: "))
    if a % 2 == 0:
        suma += a
print(f"Suma parnih brojeva je: {suma}")
