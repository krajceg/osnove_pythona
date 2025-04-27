# Zadatak
# Napisati program koji u sebi ima definisan niz od 10 broja (brojevi su proizvoljni)
# i koji menja vrednost elementa na pozciji K. K i novu vrednost unosi korisnik.
# Primer:
# Unesite pozicjiu od 0 do 9: 3
# Unesite novu vrednost: 11
# Element na 3. poziciji treba na kraju da ima vrednost 11 u vasem programu.

niz = [1, 3, 5, 6, 9, 10, 2, 4, 7, 8]

k = int(input("Unesite pozociju od 0 do 9: "))
novaVrednost = int(input("Unesite novu vrednost: "))

niz[k] = novaVrednost
print(niz)
