# (Za vezbanje) Napisati program koji ucitava N brojeva od korisnika i prikazuje koliko je K brojeva uneto.N i K unosi korisnik
# Unesite N: 4
# Unesite K: 1
# Unesite broj: 1
# Unesite broj: 2
# Unesite broj: 4
# Unesite broj: 1
# 	Uneto je 2 broja koja imaju vrednost 1. (jer su unete dve jedinice)
# Koristiti while petlju

n = int(input("Unesite broj N: "))
k = int(input("Unesite broj K: "))
counter = 0

while n > 0:
    n -= 1
    a = int(input("Unesite beroj: "))
    if a == k:
        counter += 1

print(f"Uneto je {counter} broja koji imaju vrednost {k}.")
