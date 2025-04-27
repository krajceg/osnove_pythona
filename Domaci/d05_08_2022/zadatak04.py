# Napisati program koji od korisnika ucitava N brojeva i na kraju ispisuje srednju vrednost svih brojeva.
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 2
# Unesite broj: 9
# Unesite broj: 6
# Unesite broj: 8
# Srednja vrednost je 5.
# 5 jer je celobrojno deljenje!

suma = 0
n = int(input("Unesite N: "))

for i in range(n):
    a = int(input("Unesite broj: "))
    suma += a

srednja_vrednost = round(suma / n)

print(f"Srednja vrednost je {srednja_vrednost}.")
