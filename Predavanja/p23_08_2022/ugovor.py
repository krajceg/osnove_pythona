from fizicko_lice import FizickoLice


class Ugovor():
    def __init__(self, godina: int, mesec: int, dan: int, osobaProdavac: FizickoLice, osobaKupac: FizickoLice, cena: int,
                 ulica: str, broj: int, grad: str):
        if isinstance(godina, int) and 1900 <= godina <= 2100:
            self.__godina = godina
        else:
            raise ValueError("Godina nije validna!")

        if isinstance(mesec, int) and 1 <= mesec <= 12:
            self.__mesec = mesec
        else:
            raise ValueError("Mesec nije validan!")

        if isinstance(dan, int) and 1 <= dan <= 31:
            self.__dan = dan
        else:
            raise ValueError("Dan nije validan!")

        if isinstance(osobaProdavac, FizickoLice):
            self.__osobaProdavac = osobaProdavac
        else:
            raise ValueError("Osoba nije validna!")

        if isinstance(osobaKupac, FizickoLice):
            self.__osobaKupac = osobaKupac
        else:
            raise ValueError("Osoba nije validna!")

        if isinstance(cena, int) and cena > 0:
            self.__cena = cena
        else:
            raise ValueError("Cena nije validna!")

        if isinstance(ulica, str) and ulica.strip():
            self.__ulica = ulica
        else:
            raise ValueError("Ulica nije validna!")

        if isinstance(broj, int) and broj > 0:
            self.__broj = broj
        else:
            raise ValueError("Broj prebivalista nije validan!")

        if isinstance(grad, str) and grad.strip():
            self.__grad = grad
        else:
            raise ValueError("Nije validan")

    # Getters:

    def get_godina(self):
        return self.__godina

    def get_mesec(self):
        return self.__mesec

    def get_dan(self):
        return self.__dan

    def get_osobaProdavac(self):
        return self.__osobaProdavac

    def get_osobaKupac(self):
        return self.__osobaKupac

    def get_cena(self):
        return self.__cena

    def get_ulica(self):
        return self.__ulica

    def get_broj(self):
        return self.__broj

    def get_grad(self):
        return self.__grad

    # Setters

    def set_godina(self, godina: int):
        if isinstance(godina, int) and 1900 <= godina <= 2100:
            self.__godina = godina
        else:
            raise ValueError("Godina nije validna!")

    def set_mesec(self, mesec: int):
        if isinstance(mesec, int) and 1 <= mesec <= 12:
            self.__mesec = mesec
        else:
            raise ValueError("Mesec nije validan!")

    def set_dan(self, dan: int):
        if isinstance(dan, int) and 1 <= dan <= 31:
            self.__dan = dan
        else:
            raise ValueError("Dan nije validan!")

    def set_osobaKupac(self, osobaKupac: FizickoLice):
        if isinstance(osobaKupac, FizickoLice):
            self.__osobaKupac = osobaKupac
        else:
            raise ValueError("Osoba nije validna!")

    def set_cena(self, cena: int):
        if isinstance(cena, int) and cena > 0:
            self.__cena = cena
        else:
            raise ValueError("Cena nije validna!")

    # Additional Methods:

    def procenatZarade(self):
        return 0.02 if self.__osobaKupac.get_kupovao() else 0.03

    def racunaZaraduAgencije(self):
        return round(1000 + (self.__cena * self.procenatZarade()))

    def stampaUgovor(self):
        print(
            f"{self.__dan}.{self.__mesec}.{self.__godina}. sklopljen je ugovor izmedju ", end="")
        self.__osobaProdavac.stampaj()
        print("i ", end="")
        self.__osobaKupac.stampaj()
        print(
            f"o kupovini nekretnine {self.__ulica} {self.__broj}., {self.__grad} po ceni od {self.__cena} dinara ", end="")
        print(
            f"pri cemu je kupac u obavezi da agenciji isplati novnacnu vrednost u iznosu od {self.racunaZaraduAgencije()} dinara.")
