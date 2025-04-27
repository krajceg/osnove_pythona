# Napisati program koji od korisnika ucitava N jednocifrenih brojeva i od njih formira rezultujuci broj kao na primeru
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 2
# Unesite broj: 0
# Unesite broj: 4
# Unesite broj: 1
# Rezultujuci broj je 12041

suma = ""
n = int(input("Unesite N: "))

for i in range(n):
    a = str(input("Unesite broj: "))
    suma += a

suma = int(suma)
print(f"Rezultujuci broj je {suma}")
