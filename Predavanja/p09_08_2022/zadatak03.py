# Zadatak
# Napisati program koji u sebi ima definisan niz od 5 broja (brojevi su proizvoljni)
# i koji zamenjuje vrednosti prvog (na poziciji nula) i zadnjeg elemnta niza.

niz = [1, 3, 4, 5, 6]

niz[0], niz[-1] = niz[-1], niz[0]

print(niz)
