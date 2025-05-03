from korisnik import Korisnik
from zoom_call import ZoomCall

k1 = Korisnik("Svetolik", "Kljajic")
k2 = Korisnik("Pera", "Peric")

zc1 = ZoomCall("zoomcall.com/45jb23f", "pw12345", k1, k2)

k1.pretplati(150)
k2.pretplati(100)

zc1.pokreniPoziv()
k1.ponistiPretplatu()
zc1.pokreniPoziv()
