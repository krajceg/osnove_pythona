class Video:
    def __init__(self, videoId: str = None, nazivVidea: str = None, duzinaVidea: int = None, brojLajkova: int = 0, brojDisLajkova: int = 0, brojPregleda: int = 0):

        if id is None or isinstance(videoId, str):
            self.__videoId = videoId
        else:
            raise ValueError("ID videa mora biti string!")

        if nazivVidea is None or isinstance(nazivVidea, str):
            self.__nazivVidea = nazivVidea
        else:
            raise ValueError("Naziv videa mora biti string!")

        if duzinaVidea is None or isinstance(duzinaVidea, int):
            self.__duzinaVidea = duzinaVidea
        else:
            raise ValueError("Duzina videa mora bit integer!")

        if isinstance(brojLajkova, int):
            self.__brojLajkova = brojLajkova
        else:
            raise ValueError("Broj lajkova mora bit integer!")

        if isinstance(brojDisLajkova, int):
            self.__brojDisLajkova = brojDisLajkova
        else:
            raise ValueError("Broj dislajkova mora bit integer!")

        if isinstance(brojPregleda, int):
            self.__brojPregleda = brojPregleda
        else:
            raise ValueError("Broj pregleda mora bit integer!")

    # Getters:

    def get_id(self):
        return self.__videoId

    def get_nazivVidea(self):
        return self.__nazivVidea

    def get_duzinaVidea(self):
        return self.__duzinaVidea

    def get_brojLajkova(self):
        return self.__brojLajkova

    def get_brojDislajkova(self):
        return self.__brojDisLajkova

    def get_brojPregleda(self):
        return self.__brojPregleda

    # Additional methods:

    def lajkuj(self):
        self.__brojLajkova += 1

    def disLajkuj(self):
        self.__brojDisLajkova += 1

    def pogledaj(self):
        self.__brojPregleda += 1
