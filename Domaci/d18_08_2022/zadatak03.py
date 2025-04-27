from SmartAirConditioningFile import smartAirConditioning

klima1 = smartAirConditioning()
klima1.markaKlime = "Samsung"
klima1.potrosnjaDokHladi = 1
klima1.potrosnjaDokGreje = 2
klima1.temperatura = 19
klima1.mod = "greje"

klima1.stampaj()
print(f"Ukupna mesecna potrosnja: {klima1.racunaMesecnuPotrosnju()}kW")
print(
    f"Ukupna cena mesecne potrosnje: {klima1.racunaKolikoNovcaPotrosi()} dinara")
print()

klima2 = smartAirConditioning()
klima2.markaKlime = "LG"
klima2.potrosnjaDokHladi = 1
klima2.potrosnjaDokGreje = 2
klima2.temperatura = 16
klima2.mod = "hladi"

klima2.stampaj()
print(f"Ukupna mesecna potrosnja: {klima2.racunaMesecnuPotrosnju()}kW")
print(
    f"Ukupna cena mesecne potrosnje: {klima2.racunaKolikoNovcaPotrosi()} dinara")
