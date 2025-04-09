from proizvodi import proizvod

proizvod1 = proizvod("Brasno", 60, 1000)
proizvod2 = proizvod("Slanina", 1450, 700)

proizvod1.stampaj()
proizvod2.stampaj()

print(proizvod1.konverzija("kg"))
print(proizvod2.konverzija("t"))
