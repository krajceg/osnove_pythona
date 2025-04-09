from automobili import auto

auto1 = auto("Svetolik Kljajic", "BMW", 5, 10, 200, 2022, 6, 3000)

auto1.stampaj()
ograninjenje = 130
prekoracio = auto1.prekoracioBrzinu(ograninjenje)

if prekoracio == True:
    print(
        f"Vozac je prekoracio brzinu i bice kaznjen sa {auto1.visinaKazne(ograninjenje)} dinara.")

print(auto1.oldtajmer())
print(f"Da li je istekla registracija: {auto1.isteklaRegistracija(12)}")
print(f"Cena registracije je: {auto1.cenaRegistracije()} dinara")
