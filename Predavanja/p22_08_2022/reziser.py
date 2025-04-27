class Reziser:
    def __init__(self, ime_prezime=None, starost=None):
        self.__ime_prezime = ime_prezime
        self.__starost = starost

    def get_ime_prezime(self):
        return self.__ime_prezime

    def get_starost(self):
        return self.__starost

    def set_ime_prezime(self, ime_prezime):
        if isinstance(ime_prezime, str):
            self.__ime_prezime = ime_prezime
        raise ValueError("Ime i prezime moraju biti string.")

    def set_starost(self, starost):
        if isinstance(starost, int):
            self.__starost = starost
        raise ValueError("Starost mora biti broj.")

    def stampaj(self):
        print(f"Reziser: {self.__ime_prezime}, {self.__starost} godina.")
