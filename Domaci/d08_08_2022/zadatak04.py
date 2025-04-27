# Zadatak (ZA VEZBANJE)
# Napisati program koji od korisnika ucitava stanje na racunu a zatim sa
# racuna skida dok god ima sredstava za transakciju. U slucaju da nema dovoljno sredstava ispisati odgovarajucu gresku.
# Primer izvrsenja:
# Unesite stanje na racunu: 100
# Na racunu imate $100, Unesite sumu za sledecu transakciju: 50
# Na racunu imate $50, Unesite sumu za sledecu transakciju: 31
# Na racunu imate $19, Unesite sumu za sledecu transakciju: 20
# Nemate dovoljno sredstava na racunu.Na racunu vam je ostalo $19

stanje_na_racunu = int(input("Unesite stanje na racunu: "))
suma_za_transakciju = 0

while stanje_na_racunu > suma_za_transakciju:
    suma_za_transakciju = int(input(
        f"Na racunu imate ${stanje_na_racunu}, Unesite sumu za sledecu transakciju: "))
    if stanje_na_racunu < suma_za_transakciju:
        print(
            f"Nemate dovoljno sredstava na racunu. Na racunu vam je ostalo: ${stanje_na_racunu}")
    else:
        stanje_na_racunu = stanje_na_racunu - suma_za_transakciju
        suma_za_transakciju = 0
