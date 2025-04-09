# Zadatak
# Napisati metodu koja proverava da li je trougao pravougli. Metoda prima stranice trougla i hipotenuzu trougla.
# Ako je trougao pravougli onda vraca true, u suptrotnom vraca false.
# Trougao je pravougli ukoliko je a*a+b*b=c*c

def proveraTrougla(a, b, c):
    if (a*a + b*b) == c * c:
        return True
    else:
        return False


a = 3
b = 4
c = 5
print(proveraTrougla(a, b, c))
