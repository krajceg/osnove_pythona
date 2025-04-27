from automobili import auto

auto1 = auto()
auto1.imeIPrezime = "Svetolik Kljajic"
auto1.markaAutomobila = "BMW"
auto1.brojVrata = 5
auto1.potrosnja = 10
auto1.maxBrzine = 240
auto1.trenutnaBrzina = 240
auto1.godinaProizvodnje = 2023
auto1.mesecDoKadJeRegistrovan = 12
auto1.kubikaza = 2000
auto1.brojRegistracije = "KS 207 DK"
auto1.daLiJeKlimaUkljucena = False
auto1.kapacitetGoriva = 100
auto1.trenutnaKolicinaGoriva = 50

auto1.stampaj()
ograninjenje = 130
prekoracio = auto1.prekoracioBrzinu(ograninjenje)

if prekoracio == True:
    print(
        f"Vozac je prekoracio brzinu i bice kaznjen sa {auto1.visinaKazne(ograninjenje)} dinara.")

if auto1.oldtajmer == True:
    print("Auto je oldtimer")
else:
    print("Auto nije oldtimer")

print(f"Da li je istekla registracija: {auto1.isteklaRegistracija(3)}")
print(f"Cena registracije je: {auto1.cenaRegistracije()} dinara")

# auto1.dodajGas()
# auto1.dodajGas()
# auto1.koci()

print(f"Trenutna brzine je {auto1.trenutnaBrzina} km/h")
print(f"Trenutna potrosnja je {auto1.trenutnaPotrosnjAuta()}l")
auto1.stampajTablu()
print(f"Trenutna kolicina goriva je: {auto1.trenutnaKolicinaGoriva}")
print(
    f"Kapacitet rezervoara {auto1.markaAutomobila} je: {auto1.kapacitetGoriva}")

# auto1.stampaj()

print(f"Cena natocenog goriva je: {auto1.natociGorivo(20)}")
print(f"Nova kolicina goriva je: {auto1.trenutnaKolicinaGoriva}")
