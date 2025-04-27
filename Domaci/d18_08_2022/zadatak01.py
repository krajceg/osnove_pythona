from Proizvodi import proizvod

proizvod1 = proizvod()

proizvod1.nazivProizvoda = "Brasno"
proizvod1.cenaProizvoda = 75
proizvod1.tezinaProizvodaUGramima = 100

proizvod1.stampaj()
proizvod1.povecajCenu(25)
proizvod1.stampaj()

print(f"Cena sa 30% popustom: {proizvod1.vratiCenuSaPopustom(30)}")
print(f"Postarina iznosi: {proizvod1.racunajPostarinu()}din")
print()

proizvod2 = proizvod()
proizvod2.nazivProizvoda = "Kisela Voda"
proizvod2.cenaProizvoda = 60
proizvod2.tezinaProizvodaUGramima = 2000

proizvod2.stampaj()
proizvod2.povecajCenu(10)

print(f"Cena sa 50% popustom: {proizvod2.vratiCenuSaPopustom(50)}")
print(f"Postarina iznosi: {proizvod2.racunajPostarinu()}din")
