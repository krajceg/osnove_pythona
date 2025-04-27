from kupac import Kupac


class Proizvod:
    def __init__(self, naziv=None, kupac=None, cena=None):
        self.__naziv = naziv
        if kupac is None or isinstance(kupac, Kupac):
            self.__kupac = kupac
        else:
            raise ValueError("Kupac mora biti objekat klase Kupac")

        if isinstance(cena, (int, float)):
            self.__cena = cena
        else:
            raise ValueError("Cena mora biti broj!")

    def get_naziv(self):
        return self.__naziv

    def get_kupac(self):
        return self.__kupac

    def get_cena(self):
        return self.__cena

    def set_naziv(self, naziv):
        self.__naziv = naziv

    def set_kupac(self, kupac):
        if isinstance(kupac, Kupac):
            self.__kupac = kupac

    def set_cena(self, cena):
        if isinstance(cena, (int, float)):
            self.__cena = cena
        else:
            raise ValueError("Cena mora biti broj!")

    def cenaProizvoda(self):
        return (self.__cena * 1.9 * (100 - self.__kupac.get_clanskaKarta().get_popust()) / 100)

    def stampanjeProizovda(self):
        print(f"{self.__naziv} - {self.cenaProizvoda()}")
        self.__kupac.stampaj()
