# Napisati program koji od korisnika ucitava N brojeva  i ispisuje sumu tih brojeva.
# N nam kaze koliko broja ce korisnik da unese.
# Primer izvrsenja:
# Unesite N: 3
# Unesite broj: 1
# Unesite broj: 4
# Unesite broj: 9
# Suma je 14.

suma = 0
n = int(input("Unesite broj n: "))

for i in range(n):
    a = int(input("Unesite broj: "))
    suma += a
print(f"Suma je: {suma}.")
