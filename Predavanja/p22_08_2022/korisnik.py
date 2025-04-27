class Korisnik:
    def __init__(self, ime=None, prezime=None):
        self.__ime = ime
        self.__prezime = prezime

    def get_ime(self):
        return self.__ime

    def get_prezime(self):
        return self.__prezime

    def set_ime(self, ime):
        self.__ime = ime

    def set_prezime(self, prezime):
        self.__prezime = prezime

    def stampaj(self):
        print(f"{self.__ime} {self.__prezime}")
