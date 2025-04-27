# Zadatak
# Napisati program koji od korisnika trazi da unosi brojeve sve dok ne unese nulu. U ovom programu nemamo N kao u proslom zadataku.
# Primer:
# Unesite broj: 1
# Unesite broj: 3
# Unesite broj: 5
# Unesite broj: 0
# Posto je uneta nula, to je kraj.

n = 1

while n != 0:
    n = int(input("Unesite broj n: "))

print("Posto je uneta nula, to je kraj.")
