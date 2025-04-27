from clanskaKarta import ClanskaKarta


class Kupac:
    def __init__(self, ime=None, prezime=None, clanskaKarta=None):
        if ime is None or isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime mora biti string!")

        if prezime is None or isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime mora biti string!")

        if clanskaKarta is None or isinstance(clanskaKarta, ClanskaKarta):
            self.__clanskaKarta = clanskaKarta
        else:
            raise ValueError(
                "Clanska karta mora biti objekat klase Clanska Karta")

    def get_ime(self):
        return self.__ime

    def get_prezime(self):
        return self.__prezime

    def get_clanskaKarta(self):
        return self.__clanskaKarta

    def set_ime(self, ime):
        if isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime mora biti string!")

    def set_prezime(self, prezime):
        if isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime mora biti string!")

    def stampaj(self):
        print(
            f"{self.__ime} {self.__prezime} - {self.__clanskaKarta.get_brojKartice()}")
