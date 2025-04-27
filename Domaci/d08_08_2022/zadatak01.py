# Napisati program koji ucitava N brojeva od korisnika i sabira samo trocifrene brojeve. Z
# adatak resiti while petljom.
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 32
# Unesite broj: 121
# Unesite broj: 1333
# Unesite broj: 144
# Suma je: 265

n = int(input("Unesite broj N: "))
suma = 0

while n > 0:
    a = int(input("Unesite broj: "))
    if 100 <= a < 1000:
        suma += a
    n -= 1

print(f"Suma je {suma}.")
