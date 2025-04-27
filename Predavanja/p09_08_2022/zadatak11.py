#  (Za vezbanje) Napisati program koji vrsi mesanje niza. Niz je duzine 10, proizvoljnih brojeva.
# Mesanje niza se vrsi tako sto se 8 puta vrsi zamena dva random elementa iz niza.
# primer jedne zamene:
# Ako je niz
# 1,2,3,4,5,6,7,8,9,10
# i prvi random indeks je 4 a drugi random indeks je 6
# 1,2,3,4,7,6,5,8,9,10

import random

niz = [1, 3, 5, 6, 9, 10, 2, 4, 7, 8]
print(niz)

for i in range(8):
    a, b = random.sample(range(10), 2)

    niz[a], niz[b] = niz[b], niz[a]
    print(niz)
