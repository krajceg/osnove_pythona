# Zadatak
# Napisati program koji ucitava stranice trougla a, b i c i ispisuje da li je trougao pravougli. Trougao je pravougli ako je
# Primer izvrsenja 1:
# Unesite a: 3
# Unesite b: 4
# Unesite c: 5
# Trougao je pravougli

# Primer izvrsenja 2:
# Unesite a: 3
# Unesite b: 4
# Unesite c: 6
# Trougao nije pravougli

a = int(input("Unesite a: "))
b = int(input("Unesite b: "))
c = int(input("Unesite c: "))

if (a*a) + (b*b) == c * c:
    print("Trougao je pravougli")
else:
    print("Trouglao nije pravougli")
