# Napisati program koji od korisnika ucitava 2 cela broja A i B .
# Program stampa sve brojeve od 1 do 10 osim brojeva A i B
# Primer izvrsenja:
# Unesite a: 3
# Uneiste b: 5
# 1, 2, 4, 6, 7, 8, 9, 10 => (objasnjenje: 3 i 5 nisu odstampani)

a = int(input("Unesi a: "))
b = int(input("Unesi b: "))

for i in range(1, 11):
    if i not in (a, b):
        print(i, end=", ")
