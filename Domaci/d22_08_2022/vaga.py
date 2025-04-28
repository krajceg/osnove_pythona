from proizvod import Proizvod


class Vaga:
    def __init__(self, mernaJedinica=None, proizvod: Proizvod = None):
        self.__mernaJedinica = mernaJedinica
        if isinstance(proizvod, Proizvod):
            self.__proizvod = proizvod

    # Getters:
    def get_mernajedinica(self):
        return self.__mernaJedinica

    def get_proizvod(self):
        return self.__proizvod

    # Setters:
    def set_mernaJedinica(self, mernaJedinica):
        self.__mernaJedinica = mernaJedinica

    def set_proizvod(self, proizvod):
        self.__proizvod = proizvod

    # Additional methods:
    def sracunajCenu(self, tezina):
        if self.__mernaJedinica == "kg":
            return tezina * self.__proizvod.getCenaKg()
        else:
            return tezina * self.__proizvod.getCenaLb()

    def print(self, tezina):
        self.__proizvod.print()
        if self.__mernaJedinica == "kg":
            print(
                f"{self.__proizvod.getCenaKg()} din/{self.__mernaJedinica} x {tezina}kg")
        else:
            print(
                f"{self.__proizvod.getCenaLb()} din/{self.__mernaJedinica} x {tezina}lb")
        print(f"Ukupno: {self.sracunajCenu(tezina)} din.")
