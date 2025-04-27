# Napisati porogram koji od korisnika ucitava dva broja M i N i stampa sve brojeve izmedju M i N. Smatrajte da je M manje od N.
# Primer izvrsenja:
# Unesite M: 10
# Unesite N: 15
# 10, 11, 12, 13, 14, 15,
# Print da vam bude u jednom redu i sa zarezima!

m = int(input("Unesite m: "))
n = int(input("Unesite n: "))

for i in range(m, n+1):
    print(i, end=", ")
