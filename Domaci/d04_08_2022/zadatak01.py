# Napisati program koji za ucitava brojeve a i b (b ima vrednosti 1 ili 2) Ukoliko se za b unese:
# b=1, vrednost promenljive a se uvecava za 10
# b=2, vrednost promenljive a se smanjuje za 20
# Na kraju zadatka odstampati novu vrednost promenljive a.
# 	Primer izvrsenja:
# 	Unesite a: 44
# 	Unesite b: 2
# 	Nova vrednost za a je 24

a = int(input("Unesite vrednost promenljive a: "))
b = int(input("Unesite vrednost promenljive b: "))

if b == 1:
    a += 10
elif b == 2:
    a -= 20

print(f"Nova vrednost za a je {a}")
