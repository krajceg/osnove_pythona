# Napisati program koji simulira stampanje ocitane licne karte u vise primeraka. Korisnik unosi podatke :
# ime
# prezime
# jmbg
# broj primeraka za stampu
# Primer izvrsenja:
# Unesite ime: Milan
# Unesite prezime: Jovanovic
# Unesite jmbg: 2109238932232
# Unesite broj primeraka za stampu: 3
# Primerak 1
# **********************************
# Ime i prezime: Milan Jovanovic
# JMBG: 2109238932232
# **********************************

ime = str(input("Unesite ime: "))
prezime = str(input("Unesite prezime: "))
jmbg = int(input("Unesite jmbg: "))
brojPrimeraka = int(input("Unesite broj primeraka za stampu: "))

for i in range(brojPrimeraka):
    print(f"Primerak: {i+1}")
    print("*******************************")
    print(f"Ime i prezime: {ime} {prezime}")
    print(f"JMBG: {jmbg}")
    print("*******************************")
    print()
