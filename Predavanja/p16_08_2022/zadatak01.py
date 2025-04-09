# 1.Zad
# //		Kreirati klasu Racun koja ima
# //		broj racuna (npr: 840-23932-323)
# //		ime i prezime vlasnika
# //		stanje na racunu
# //		U mainu kreirati minimum dva racuna sa pratecim podacima i ostampati podatke za svaki objekat.

# Dopuniti zadatak tako da se vrsi transakcija sa prvog na drugi racun. Korisnik unosi svotu koja se skida sa prvog i prebacuje na drugi racun.

# Primer izvrsenja:
# Posaljilac: Milan Jovanovic, 840-23932-323, stanje: 1000
# Primalac: Marko Markovic, 840-23932-334, stanje: 200
# Unesite sumu za transakciju: 500
# Stanje nakon stransakcije
# Posaljilac: Milan Jovanovic, 840-23932-323, stanje: 500
# Primalac: Marko Markovic, 840-23932-334, stanje: 700

from racuni import racun

r1 = racun("840-222-333-444", "Svetolik Kljajic", 1000)
r2 = racun("140-555-666-111", "Mitar Miric", 200)

print(f"Posiljalac: {r1.imePrezime}, {r1.brojRacuna}, {r1.stanje}")
print(f"Primalac: {r2.imePrezime}, {r2.brojRacuna}, {r2.stanje}")

svota = int(input("Unesite svotu za transakciju: "))

r1.stanje = r1.stanje-svota
r2.stanje = r2.stanje+svota

print("Stanje nakon transakcije: ")
print(f"Posiljalac: {r1.imePrezime}, {r1.brojRacuna}, {r1.stanje}")
print(f"Primalac: {r2.imePrezime}, {r2.brojRacuna}, {r2.stanje}")
