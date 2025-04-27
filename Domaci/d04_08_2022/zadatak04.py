# Napisati program koji za unetu vrednost x odredjuje i prikazuje vrednost funkcije y.
# Iskoristite if/else za racunanje informacije i tek nakon te logike odstampajte vrednost y na ekranu.Funkcija y je definisana kao:
#     			       (x,       x < 2
# y =                  (2,      2 <= x < 10
#     			       (x - 1, x >= 10

# Objasnjenje formule: Ako je x manje od 2, y je jednako x
# 			 Ako je x u opsegu od 2 do 10, y je jednako 2
# 			 Ako je x vece od 10, y je x-1

x = int(input("Unesite x: "))

if x < 2:
    y = x
elif 2 <= x < 10:
    y = 2
else:
    y = x - 1

print(f"Vrednost y je: {y}")
