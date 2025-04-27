from proizvod import Proizvod
from kupac import Kupac
from clanskaKarta import ClanskaKarta

ck1 = ClanskaKarta(5, 444555)

k1 = Kupac("Svetolik", "Kljajic", ck1)

p1 = Proizvod("Kafa", k1, 1800)

p1.stampanjeProizovda()
