class FizickoLice():
    def __init__(self, ime: str, prezime: str, brojLicneKarte: int, jmbg: int, kupovao: bool):
        if isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime nije validno!")

        if isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime nije validno!")

        if isinstance(brojLicneKarte, int):
            self.__brojLicneKarte = brojLicneKarte
        else:
            raise ValueError("Broj licne nije validan!")

        if isinstance(jmbg, int):
            self.__jmbg = jmbg
        else:
            raise ValueError("JMBG nije validan!")

        if isinstance(kupovao, bool):
            self.__kupovao = kupovao
        else:
            raise ValueError("Kupovao nije validan!")

    # Getters:
    def get_ime(self):
        return self.__ime

    def get_prezime(self):
        return self.__prezime

    def get_brojLicneKarte(self):
        return self.__brojLicneKarte

    def get_jmbg(self):
        return self.__jmbg

    def get_kupovao(self):
        return self.__kupovao

    # Setters:
    def set_ime(self, ime: str):
        if isinstance(ime, str):
            self.__ime = ime
        else:
            raise ValueError("Ime nije validno!")

    def set_prezime(self, prezime: str):
        if isinstance(prezime, str):
            self.__prezime = prezime
        else:
            raise ValueError("Prezime nije validno!")

    def set_brojLicneKarte(self, brojLicneKarte: int):
        if isinstance(brojLicneKarte, int):
            self.__brojLicneKarte = brojLicneKarte
        else:
            raise ValueError("Broj licne nije validan!")

    def set_kupovao(self, kupovao: bool):
        if isinstance(kupovao, bool):
            self.__kupovao = kupovao
        else:
            raise ValueError("Kupovao nije validan!")

    # Additional methods:
    def stampaj(self):
        print(f"{self.__ime} {self.__prezime}, {self.__brojLicneKarte}", end=" ")
