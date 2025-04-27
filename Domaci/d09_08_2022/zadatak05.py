# (Za vezbanje) Napisati program koji ucitava niz stringova duzine N,
# tako da ucitavanje elemenata u niz a bude obrnuto.
# Primer:
#     Unesite N: 4
#     Unesite string: xxx1
#     Unesite string: xxx4
#     Unesite string: xxx6
#     Unesite string: xxx9

#     Niz a: xxx9, xxx6, xxx4, xxx1
#     Komentar: Stanje niza a u memoriji je:
#         a[0] = "xxx9",
#         a[1] = "xxx6",
#         a[2] = "xxx4",
#         a[3] = "xxx1",

n = int(input("Unesite broj n: "))
niz = [str(input("Unesite string: ")) for _ in range(n)][::-1]

# niz = []
# for _ in range(n):
#     niz.insert(0, str(input("Unesite string: ")))

print(f"Niz a: {niz}")
