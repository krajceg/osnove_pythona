# Napisati program koji sa tastature ucitava ime, prezime, broj telefona, email. korisnika i prikazuje u formatu:
# [Ime] [Prezime] - [JMBG]
# Broj Tel: [Broj telefona],
# Email: [Email],

# Unesite ime: Milan
# Unesite prezime: Jovanvoci
# Unesite broj: +209329832
# Unesite email: milan@gmail.com
# Unesite jmbg: 329032938923

# Milan Jovanovic - 329032938923
# Broj tel:  +209329832
# Email: milan@gmail.com

ime = str(input("Unesite ime: "))
prezime = str(input("Unesite prezime: "))
jmbg = str(input("Unesite JMBG: "))
brojTel = str(input("Unesite broj telefona: "))
email = str(input("Unesite email: "))

print(f"{ime} {prezime} - {jmbg}")
print(f"Broj telefona: {brojTel}")
print(f"Email: {email}")
