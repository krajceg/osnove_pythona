# Napisati program za potrebe Makao igrice. Korisnik unosi 4 informacije:
# znak karte koja je na stolu
# broj karte koja je na stolu
# znak karte koju igrac zeli da odigra
# broj karte koju igrac zeli da odigra
# 	i nakon toga se na ekranu ispisuje da li je potez ispravan. Potez je ispravan ukoliko se karta
# na stolu i odigrana karta poklapaju po znaku ili broju.

znakKarteNaStolu = str(input("Unesite znak karte na stolu: "))
brojKarteNaStolu = str(input("Unesite broj karte na stolu: "))
znakKarteIgrac = str(input("Unesite znak karte koju zelite da odigrate: "))
brojKarteIgrac = str(input("Unesite broj karte koju zelite da odigrate: "))

if znakKarteNaStolu == znakKarteIgrac or brojKarteNaStolu == brojKarteIgrac:
    print("Potez je ispravan")
else:
    print("Potez nije ispravan")
