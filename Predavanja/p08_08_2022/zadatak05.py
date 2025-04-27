# Zadatak
# Napisati program koji validira unos input polja za broj.
# Polje za unos prima samo brojeve u opsegu od 10 do 50.Korisnik unosi vrednosti dok ne unese validan  broj.
# Primer izvrsenja:
# Unesite broj: 5
# Greska: Broj nije u opsegu od 10 do 50.
# Unesite broj: -1
# Greska: Broj nije u opsegu od 10 do 50.
# Unesite broj: 51
# Greska: Broj nije u opsegu od 10 do 50.
# Unesite broj: 40
# Broj je validan, kraj programa.

a = 1

while not 10 < a < 50:
    a = int(input("Unesite broj :"))

print("Broj je validan, kraj programa.")
