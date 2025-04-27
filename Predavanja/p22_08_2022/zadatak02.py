from korisnik import Korisnik
from facebookpost import FacebookPost

korisnik_1 = Korisnik()
korisnik_1.set_ime("Svetolik")
korisnik_1.set_prezime("Kljajic")

post_1 = FacebookPost("Pyhton is fun", korisnik_1)

post_1.print()
print(korisnik_1.get_ime())
