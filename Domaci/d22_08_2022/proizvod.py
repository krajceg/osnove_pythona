

class Proizvod():
    def __init__(self, sifraProizvoda=None, nazivProizvoda=None, cenaPoKg=None):
        self.__sifraProizvoda = sifraProizvoda
        self.__nazivProizvoda = nazivProizvoda
        self.__cenaPoKg = cenaPoKg

    # Getters:
    def get_sifraProizvoda(self):
        return self.__sifraProizvoda

    def get_nazivProizvoda(self):
        return self.__nazivProizvoda

    # Setters:
    def set_sifraProizvoda(self, sifraProizvoda):
        self.__sifraProizvoda = sifraProizvoda

    def set_nazivProizvoda(self, nazivProizvoda):
        self.__nazivProizvoda = nazivProizvoda

    def set_cenaPoKg(self, cenaPoKg):
        self.__cenaPoKg = cenaPoKg

    # Additonal methods:
    def getCenaKg(self):
        return self.__cenaPoKg

    def getCenaLb(self):
        return self.__cenaPoKg * 2.2046

    def print(self):
        print(f"{self.__sifraProizvoda} - {self.__nazivProizvoda}")
