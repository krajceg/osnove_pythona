
class Korisnik:
    def __init__(self, ime: str = None, prezime: str = None, tipLicence: str = "Basic"):
        if ime is None or isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime mora biti string!")

        if prezime is None or isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime mora biti string!")

        if tipLicence in ("Basic", "Pro", "Premium"):
            self.__tipLicence = tipLicence
        else:
            raise ValueError("Tip licence nije validan!")

    # Getters:
    def get_ime(self):
        return self.__ime

    def get_prezime(self):
        return self.__prezime

    def get_tipLicence(self):
        return self.__tipLicence

    # Setters:
    def set_ime(self, ime: str):
        if isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime mora biti string!")

    def set_prezime(self, prezime: str):
        if isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime mora biti string!")

    # Additional methods:
    def pretplati(self, suma: int):
        if isinstance(suma, int):
            if suma == 100:
                self.__tipLicence = "Pro"
            elif suma == 150:
                self.__tipLicence = "Premium"

    def ponistiPretplatu(self):
        self.__tipLicence = "Basic"

    def maxiDuzinaVideoPoziva(self):
        if self.__tipLicence == "Basic":
            return 40
        elif self.__tipLicence == "Pro":
            return 240
        elif self.__tipLicence == "Premium":
            return 1440

    def print(self):
        print(f"{self.__ime} {self.__prezime}")
