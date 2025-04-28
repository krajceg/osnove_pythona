from autor import Autor
from knjiga import Knjiga

a1 = Autor("Dobrica Cosic")

k1 = Knjiga()

k1.set_autor(a1)
k1.set_isbn("978-86-521-4415-0")
k1.set_godinaIzdavanja(2024)
k1.set_naziv("Na Drini Cuprija")

k1.print()
