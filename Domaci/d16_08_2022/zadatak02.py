from smart import smartAirConditioning

klima1 = smartAirConditioning("Samsung", 19, "hladi")
klima2 = smartAirConditioning("Bosch", 25, "greje")

klima1.stampaj()

print(klima1.napoljuVecaTemp(35))
print()
klima2.stampaj()
print(klima2.napoljuVecaTemp(3))
