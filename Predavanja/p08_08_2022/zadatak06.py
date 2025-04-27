# Zadatak
# Napisati program koji od korisnika ucitava brojeve sve dok ne unesu makar po jedan broj od 1 do 4.
# Primer:
# Unesite broj:1
# Unesite broj:2
# Unesite broj:2
# Unesite broj:3
# Unesite broj:0
# Unesite broj:5
# Unesite broj:3
# Unesite broj:4

# Kraj programa
# Objasnjenje: Od svakih brojeva: 1, 2, 3 i 4 je unet po jedan.

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

while counter1 == 0 or counter2 == 0 or counter3 == 0 or counter4 == 0:
    a = int(input("Unesite broj: "))
    if a == 1:
        counter1 += 1
    elif a == 2:
        counter2 += 1
    elif a == 3:
        counter3 += 1
    elif a == 4:
        counter4 += 1

print("Kraj programa.")
print("Od svakih brojeva 1, 2, 3 i 4 je unet po jedan.")
