#  Zadatak
# Napisati metodu koja stampa N zvezdica u istom redu. Broj zvezdica je odredjen parametrom N.
# Ako se metoda pozove za N=5, metoda stampa 5 zvezdica i enter
# N=5, print je=> * * * * *

# (Za vezbanje)
# Napisati main program koji koristi metodu definisanu u 6.zad tako da stampa sledecu sliku za N. N unosi korisnik.


# Primer izvrsenja:
# Unesite N: 6
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *


def zvezdice(broj):
    for i in range(broj):
        print("* ", end="")


n = 6
for i in range(1, n+1):
    zvezdice(i)
    print()
