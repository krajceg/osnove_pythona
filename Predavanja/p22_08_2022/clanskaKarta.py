class ClanskaKarta:
    def __init__(self, popust=None, brojKartice=None):
        if popust is None or isinstance(popust, int):
            self.__popust = popust
        else:
            raise ValueError("Popust mora biti intiger!")

        self.__brojKartice = brojKartice

    def get_popust(self):
        return self.__popust

    def get_brojKartice(self):
        return self.__brojKartice

    def set_popust(self, popust):
        if isinstance(popust, int):
            self.__popust = popust
        else:
            raise ValueError("Popust mora biti intiger!")

    def set_brojKartice(self, brojKartice):
        self.__brojKartice = brojKartice
