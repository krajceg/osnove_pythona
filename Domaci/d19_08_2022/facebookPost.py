class FacebookPost():
    def __init__(self, ime_i_prezime_objavio=None, ime_i_prezime_profila=None, tekst=None, broj_lajkova=None, broj_deljenja=None):
        self.__ime_i_prezime_objavio = ime_i_prezime_objavio
        self.__ime_i_prezime_profila = ime_i_prezime_profila
        self.__tekst = tekst
        self.__broj_lajkova = broj_lajkova
        self.__broj_deljenja = broj_deljenja

    def like(self):
        self.__broj_lajkova += 1

    def dislike(self):
        self.__broj_lajkova = max(0, self.__broj_lajkova - 1)

    def share(self):
        self.__broj_deljenja += 1

    def print(self):
        print(f"{self.__ime_i_prezime_objavio} >>> {self.__ime_i_prezime_profila}")
        print(self.__tekst)
        print(f"Likes {self.__broj_lajkova} | Shares {self.__broj_deljenja}")
