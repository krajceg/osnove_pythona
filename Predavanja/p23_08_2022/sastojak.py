class Sastojak:
    def __init__(self, naziv: str = None, cena: int = None):
        if naziv is None or isinstance(naziv, str):
            self.__naziv = naziv
        else:
            raise ValueError("Naziv nije validan!")
        if cena is None or (isinstance(cena, int) and cena > 0):
            self.__cena = cena
        else:
            raise ValueError("Cena nije validna")

    # Getters:

    def get_naziv(self):
        return self.__naziv

    def get_cena(self):
        return self.__cena

    # Setters:

    def set_naziv(self, naziv: str):
        if isinstance(naziv, str):
            self.__naziv = naziv
        else:
            raise ValueError("Naziv nije validan!")

    def set_cena(self, cena: int):
        if isinstance(cena, int) and cena > 0:
            self.__cena = cena
        else:
            raise ValueError("Cena nije validna!")

    # Additional methods:

    def stampaj(self):
        print(f"Naziv: {self.__naziv}, cena: {self.__cena}")
