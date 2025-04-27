# Napisati program koji od korisnika ucitava jacinu zvuka (od 0 do 10) i stampa slikicu za zvuk sa brojem crtica koje je korisnik uneo.
# Primer izvrsenja;
# Unesite jacinu zvuka: 8
# < | | | | | | | |

# (Dopuna za vezbanje)
# Ukoliko je jacina zvuka 0 stampa se slika </ (simulacija za mute) u sprotnom < | | | (sa brojem crtica jacinom zvuka)

jacinaZvuka = int(input("Unesite jacinu zvuka: "))
print("<", end="")
if jacinaZvuka == 0:
    print("/")
else:
    for i in range(jacinaZvuka):
        print(" |", end="")
