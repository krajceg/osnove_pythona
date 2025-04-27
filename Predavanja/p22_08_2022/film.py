from reziser import Reziser


class Film:
    def __init__(self, naziv_filma=None, godina=None, reziser=None):
        self.__naziv_filma = naziv_filma
        self.__godina = godina

        if reziser is None or isinstance(reziser, Reziser):
            self.__reziser = reziser
        else:
            raise ValueError("Reziser mora biti objekat klase Reziser")

    def get_naziv_filma(self):
        return self.__naziv_filma

    def get_godina(self):
        return self.__godina

    def get_reziser(self):
        return self.__reziser

    def set_naziv_filma(self, naziv_filma):
        if isinstance(naziv_filma, str):
            self.__naziv_filma = naziv_filma
        raise ValueError("Film mora biti string.")

    def set_godina(self, godina):
        if isinstance(godina, int):
            self.__godina = godina
        raise ValueError("Godina mora biti broj")

    def set_reziser(self, reziser):
        if isinstance(reziser, Reziser):
            self.__reziser = reziser
        raise ValueError("Reziser mora biti objekat klase Reziser.")

    def stampaj(self):
        print(f"Film: {self.__naziv_filma} - Godina: {self.__godina}")
        self.__reziser.stampaj()
