# (za vezbanje)Napisati program koji ucitava sa tastature N karaktera i kreira niz koji
# predstavlja palindrom.Na kraju programa odstampati novo kreirani niz.
# Primer izvrsenja:
# Unesite N: 4
# Unesite karakter: M
# Unesite karakter: b
# Unesite karakter: n
# Unesite karakter: c
# Palindrom: M, b, n, c, c, n, b, M
# Napomena: U memoriji niz treba da ima sve ove elemente.

n = int(input("Unesite broj N: "))
niz = []
for i in range(n):
    a = str(input("Unesite karakter: "))
    niz.append(a)

niz_reversed = list(reversed(niz))

niz = niz + niz_reversed

print(niz)
