from korisnik import Korisnik


class FacebookPost:
    def __init__(self, opis=None, korisnik=None):
        self.__opis = opis
        if korisnik is None or isinstance(korisnik, Korisnik):
            self.__korisnik = korisnik
        else:
            raise ValueError("Korisnik mora biti objekat klase Korisnik")

    def print(self):
        self.__korisnik.stampaj()
        print(self.__opis)
