# Napisati metodu koja vrsi spajanje punog imena i vraca tu vrednost.
# Metoda od parametara prima ime i prezime (2 parametra) i vraca jedan string tako sto spoji ime i prezime. METODA NISTA NE STAMPA.
# Primer poziva: Ako se metoda pozvoe za ime=”Milan” i prezime=”Jovanovic”, metoda vraca “Milan Jovanovic”

def spajanje(ime, prezime):
    return f"{ime} {prezime}"


puno = spajanje("Svetolik", "Kljajic")
print(puno)
