# Zadatak
# Napisati progam koji stampa niz u obrnutom redosledu tj. od zadnjeg elementa do prvog.

niz = [1, 3, 5, 6, 9, 10, 2, 4, 7, 8]

for i in reversed(niz):
    print(i, end=", ")
