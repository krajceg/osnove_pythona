# Zadatak
# Napisati program koji od korisnika ucitava brojeve sve dok ne unesu dve nule.
# Primer:
# Unesite broj:1
# Unesite broj:2
# Unesite broj:0
# Unesite broj:1
# Unesite broj:0
# Kraj programa jer je uneto 2 nule.

counter = 0

while counter < 2:
    a = int(input("Unesite broj: "))
    if a == 0:
        counter += 1
print("Kraj programa jer je uneto 2 nule.")
