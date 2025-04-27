# Napisati program koji od korisnika ucitava N brojeva i te brojeve samo odsampa nakon unosa.
# Primer izvrsenja:
# Unesite N: 3
# Unesite broj: 1
# Unet broj je 1.
# Unesite broj: 4
# Unet broj je 4.
# Unesite broj: 9
# Unet broj je 9.

n = int(input("Unesite broj N: "))

while n > 0:
    a = int(input("Unesite broj: "))
    print(f"Uneti broj je {a}")
    n -= 1
