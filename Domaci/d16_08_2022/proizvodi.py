class proizvod:
    def __init__(self, nazivProizvoda, cenaProizvoda, tezinaProizvodaUGramima):
        self.nazivProizvoda = nazivProizvoda
        self.cenaProizvoda = cenaProizvoda
        self.tezinaProizvodaUGramima = tezinaProizvodaUGramima

    def stampaj(self):
        print(
            f"({self.nazivProizvoda}), ({self.cenaProizvoda}), ({self.tezinaProizvodaUGramima})")

    def konverzija(self, jedinica):
        if jedinica == "kg":
            return self.tezinaProizvodaUGramima/1000
        elif jedinica == "t":
            return self.tezinaProizvodaUGramima/1000000
