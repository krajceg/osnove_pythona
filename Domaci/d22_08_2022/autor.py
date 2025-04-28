class Autor():
    def __init__(self, imePrezime: str = None):
        if imePrezime is None or isinstance(imePrezime, str):
            self.__imePrezime = imePrezime
        else:
            raise ValueError("Ime i prezime moraju biti string!")

    # Getters
    def get_imePrezime(self):
        return self.__imePrezime

    # Setters:
    def set_imePrezime(self, imePrezime: str):
        if isinstance(imePrezime, str):
            self.__imePrezime = imePrezime
        else:
            raise ValueError("Ime i prezime moraju biti string!")

    # Additional methods:
    def print(self):
        print(self.__imePrezime)
