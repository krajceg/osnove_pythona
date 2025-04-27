# (Za vezbanje) Napisati program za ucenje matematike.
# Program daje korisniku matematicke zadatke sve dok ne pogresi.
# Svaki nivo predstavlja jednu iteraciju petlje i u svakom nivou korisniku se
# prikazuju dva random broja koja treba da sabere. (Program generise random brojeve u opsegu od 0 do 100, ne unosi ih korisnik)
# Random brojevi u Javi se generisisu kao u primeru
# // creating an object of Random class
# Random random = new Random();
# // Generates random integers 0 to 49
# int x = random.nextInt(50);

import random
rezultat = True

while rezultat == True:
    a = random.randrange(100)
    b = random.randrange(100)
    tacan_odgovor = a + b
    odgovor = int(input(f"{a} + {b} = "))
    if tacan_odgovor != odgovor:
        rezultat = False
print(f"Kraj jer ste pogresili. Tacan rezultat je: {tacan_odgovor}.")
