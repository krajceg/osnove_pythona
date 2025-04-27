class proizvod:
    def __init__(self, nazivProizvoda=None, cenaProizvoda=None, tezinaProizvodaUGramima=None):
        self.nazivProizvoda = nazivProizvoda
        self.cenaProizvoda = cenaProizvoda
        self.tezinaProizvodaUGramima = tezinaProizvodaUGramima

    def stampaj(self):
        print(
            f"({self.nazivProizvoda}), ({self.cenaProizvoda}), ({self.tezinaProizvodaUGramima})")

    def povecajCenu(self, povecanje):
        self.cenaProizvoda = self.cenaProizvoda + povecanje

    def vratiCenuSaPopustom(self, popust):
        # return round((self.cenaProizvoda - (self.cenaProizvoda*popust/100)), 2)
        return round((self.cenaProizvoda*(100-popust)/100), 2)

    def racunajPostarinu(self):
        if self.tezinaProizvodaUGramima <= 100:
            return 200
        elif self.tezinaProizvodaUGramima <= 500:
            return 400
        else:
            return 1000
