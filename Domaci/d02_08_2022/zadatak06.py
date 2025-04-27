# Napisati program koji ima informacije koje ucitava informacije sa tastature:
# Ime
# Prezime
# godinu rodjenja
# I stampa informaicije u formatu:
# [ime] [prezime] - [startost] god

# Primer izvrsenja:
# Ako je ime = Milan, prezime = Jovanovic i godina rodjenja 1995 stapaju se informacije
# Milan Jovanovic - 26 god

ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
godRodjenja = int(input("Unesite godinu rodjenja: "))

print(f"{ime} {prezime} - {2025-godRodjenja}")
