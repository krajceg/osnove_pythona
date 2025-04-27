# Napisati program koji sa tastature ucitava sledece podatke:
# pol osobe
# cena proizvoda
# da li je proizvod neophodan (unosimo da ili ne)
# I na kraju ispisuje informaciju da li ce se proizvod kupiti.
# Proizvod se kupuje ako je pol osobe zenski i proizvod je neophodan, nezavisno od cene proizvoda.

polOsobe = str(input("Unesite pol: "))
cenaProizvoda = int(input("unesite cenu proizvoda: "))
neophodan = str(input("Unesite da li je proizvod nephodan: "))

if polOsobe == "zenski" and neophodan == "da":
    print("Proizvod se kupuje")
