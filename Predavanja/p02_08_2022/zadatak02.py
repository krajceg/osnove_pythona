# Napisati program koji na ekranu stampa podatke u formatu:
# Sifra [SIFRA PROIZVODA]
# [NAZIV PROIZVODA]  - $[CENA] - Popust [POPUST]%
# [BOJA], [VELICINA]

sifraProizvoda = "1234asdf"
nazivProizvoda = "Nike sorc"
cena = 15
popust = 30
boja = "crvena"
velicina = "xl"

print(f"Sifra: {sifraProizvoda}")
print(f"{nazivProizvoda} = ${cena} - Popust {popust}%")
print(f"{boja}, {velicina}")
