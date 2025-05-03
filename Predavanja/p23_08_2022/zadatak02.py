from fizicko_lice import FizickoLice
from ugovor import Ugovor

prodavac = FizickoLice("Sinan", "Sakic", 333555999, 21412451, False)
kupac = FizickoLice("Mitar", "Miric", 44442222, 1234564566, True)

ugovor1 = Ugovor(2024, 12, 12, prodavac, kupac,
                 100000, "Ostrva Vida", 21, "Krusevac")


ugovor1.stampaUgovor()
