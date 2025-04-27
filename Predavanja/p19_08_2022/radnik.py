"""This module defines the Person class and its associated methods for checking
credit eligibility and calculating salary."""


class Radnik:
    def __init__(self, jmbg=None, ime_prezime=None, broj_dece=None, stepen_strucne_spreme=None, godine_radnog_staza=None):
        self.__jmbg = jmbg
        self.__ime_przime = ime_prezime
        self.__broj_dece = broj_dece
        self.__stepen_strucne_spreme = stepen_strucne_spreme
        self.__godine_radnog_staza = godine_radnog_staza

    def get_jmbg(self):
        return self.__jmbg

    def get_ime_prezime(self):
        return self.__ime_przime

    def get_broj_dece(self):
        return self.__broj_dece

    def get_stepen_strucne_spreme(self):
        return self.__stepen_strucne_spreme

    def get_godine_radnog_staza(self):
        return self.__godine_radnog_staza

    def set_jmbg(self, jmbg):
        if isinstance(jmbg, (int)):
            self.__jmbg = jmbg
        else:
            raise ValueError("JMBG mora biti broj.")

    def set_ime_prezime(self, ime_prezime):
        if isinstance(ime_prezime, (str)):
            self.__ime_przime = ime_prezime
        else:
            raise ValueError("Ime i prezime mora biti string.")

    def set_broj_dece(self, broj_dece):
        if isinstance(broj_dece, (int)):
            self.__broj_dece = broj_dece
        else:
            raise ValueError("Broj dece mora biti broj.")

    def set_stepen_strucne_spreme(self, stepen_strucne_spreme):
        if isinstance(stepen_strucne_spreme, (int)):
            self.__stepen_strucne_spreme = stepen_strucne_spreme
        else:
            raise ValueError("Stepen strucne spreme mora biti broj.")

    def set_godine_radnog_staza(self, godine_radnog_staza):
        if isinstance(godine_radnog_staza, (int)):
            self.__godine_radnog_staza = godine_radnog_staza
        else:
            raise ValueError("Godine radnog staza moraju biti broj.")

    def minuli_rad(self):
        if self.__godine_radnog_staza <= 10:
            return 0.05 * self.__godine_radnog_staza
        elif self.__godine_radnog_staza <= 20:
            return 0.075 * self.__godine_radnog_staza
        else:
            return 0.1 * self.__godine_radnog_staza

    def koeficijent_slozenosti(self):
        if self.__stepen_strucne_spreme == 1:
            return 1.03
        elif self.__stepen_strucne_spreme == 2:
            return 1.65
        elif self.__stepen_strucne_spreme == 3:
            return 2.00
        elif self.__stepen_strucne_spreme == 4:
            return 2.27
        elif self.__stepen_strucne_spreme == 5:
            return 2.88
        elif self.__stepen_strucne_spreme == 6:
            return 3.09
        elif self.__stepen_strucne_spreme == 7:
            return 3.40
        elif self.__stepen_strucne_spreme == 8:
            return 4.12

    def plata_radnika(self):
        return (25000 + (self.koeficijent_slozenosti() + self.minuli_rad()) * 10000)

    def kreditno_sposoban(self):
        return self.plata_radnika() > 50000
