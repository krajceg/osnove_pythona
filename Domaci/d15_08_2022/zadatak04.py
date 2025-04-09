# Zadatak
# Napisati metodu koja stampa podatke o korisniku u formatu:
# JMBG: [jmbg]
# Ime: [ime]
# Prezime: [prezime]
# God. rodjenja: [god]
# Aktivan: [true/false]
# Metoda prima jmbg, ime, prezime, god rodjenja i da li je aktivan kao parametre metode.Metoda nista ne vraca.

def podaciOKorisniku(jmbg, ime, prezime, godRodjenja, aktivan):
    print(f"JMBG: {jmbg}")
    print(f"Ime: {ime}")
    print(f"Prezime: {prezime}")
    print(f"God. rodjenja: {godRodjenja}")
    print(f"Aktivan: {aktivan}")


podaciOKorisniku(123456789, "Svetolik", "Kljajic", 1988, True)
