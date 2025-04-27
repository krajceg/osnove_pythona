# Napisati program koji ispisuje da li je broj b manji od broja a. A i B unosimo sa tastature.

a = int(input("Unesite a: "))

b = int(input("Unesite b: "))
# a = 14
# b = 2

if a > b:
    print(f"{a} je vece od {b}")
else:
    print(f"{b} je vece od {a}")
