# 12. (za vezbanje) Napisati program koji ima niz duzine 25 proizvoljnih elemenata
# i stampa niz kao tablu dimenzije 5x5.
# Primer stampe:
# 1, 2, 3, 4, 6,
# 5, 6, 7, 3, 4,
# 5, 2, 1, 4, 5,
# 6, 6, 6, 2, 1
# 1, 9, 8, 7, 6

niz = [3, 8, 1, 9, 4, 2, 7, 5, 6, 9, 1, 3,
       8, 7, 2, 4, 5, 6, 3, 9, 8, 7, 1, 4, 2]

# for i in range(len(niz)):
#     if (i) % 5 == 0:
#         print()
#     print(niz[i], end=", ")

for i, value in enumerate(niz, start=1):
    print(value, end=", ")
    if i % 5 == 0:
        print()
