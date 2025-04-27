# Napisati program koji ucitava brojeva od korisnika i za svaki broj
# prikazuje apsolutnu vrednost sve dok se ne unese nula.
# Pomoc: Apsolutna vrednost je kada bilo koji broj pretvarate u pozitivan broj.
# Npr: -2 u 2 ili -4 u 4 dok pozitivni ostaju pozitivni npr: 9 ostaje 9
# Primer izvrsenja:
# Unesite broj: 3
# Apsolutna vrednost je 3
# Unesite broj: -1
# Apsolutna vrednost je 1
# Unesite broj: 0
# Kraj programa jer je uneta nula.

n = 1

while n != 0:
    n = int(input("Unesite broj: "))
    if n != 0:
        print(f"Apsolutna vrednost je: {abs(n)}")

print("Kraj programa jer je uneta nula.")
