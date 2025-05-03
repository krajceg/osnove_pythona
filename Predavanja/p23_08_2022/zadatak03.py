from sastojak import Sastojak

s1 = Sastojak("brasno", 70)
s2 = Sastojak("so", 60)
s3 = Sastojak("voda", 40)

lista_sastojaka1 = [s1, s2, s3]
lista_sastojaka2 = []


n = int(input("Unesite broj sastojaka: "))

for i in range(n):
    naziv = str(input("Unesite naziv sastojka: "))
    m = int(input("Unesite cenu sastojka: "))
    s = Sastojak(naziv, m)
    lista_sastojaka2.append(s)

for i in range(n):
    lista_sastojaka2[i].stampaj()
