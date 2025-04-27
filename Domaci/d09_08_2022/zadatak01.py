# Zadatak
# Napisati program koji ucitava N brojeva i smesta ih u niz. Zatim, iz niza,
# broji koliko je parnih brojeva uneto. brojeve unosi korisnik.
# Unesite N: 5
# Unesite broj: 1
# Unesite broj: 3
# Unesite broj: 4
# Unesite broj: 7
# Unesite broj: 8
# U nizu ima 2 parna broja.

n = int(input("Unesite broj N: "))
niz = [int(input("Unesite broj: ")) for _ in range(n)]

even_counter = sum(1 for broj in niz if broj % 2 == 0)

print(f"U nizu ima {even_counter} parna broja.")
