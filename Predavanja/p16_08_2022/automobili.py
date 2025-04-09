class auto():
    def __init__(self, imeIPrezime, markaAutomobila, brojVrata, potrosnja, trenutnaBrzina, godinaProizvodnje, mesecDoKadJeRegistrovan, kubikaza):
        self.imeIPrezime = imeIPrezime
        self.markaAutomobila = markaAutomobila
        self.brojVrata = brojVrata
        self.potrosnja = potrosnja
        self.trenutnaBrzina = trenutnaBrzina
        self.godinaProizvodnje = godinaProizvodnje
        self.mesecDoKadJeRegistrovan = mesecDoKadJeRegistrovan
        self.kubikaza = kubikaza

    def stampaj(self):
        print(self.imeIPrezime)
        print(f"{self.markaAutomobila} - {self.brojVrata}-ro vrata")
        print(f"Sa potrosnjom od {self.potrosnja}l na 100km")
        print(f"{self.trenutnaBrzina} km/h je trenutna brzina")

    def prekoracioBrzinu(self, ogranicenje):
        if self.trenutnaBrzina > ogranicenje:
            return True
        else:
            return False

    def visinaKazne(self, ogranicenje):
        if self.prekoracioBrzinu(ogranicenje):
            return (self.trenutnaBrzina - ogranicenje) * 1000

    def oldtajmer(self):
        if self.godinaProizvodnje < 1950:
            return ("Auto je oldtajmer")
        else:
            return ("Auto nije oldtajmer")

    def isteklaRegistracija(self, trenutniMesec):
        if trenutniMesec < self.mesecDoKadJeRegistrovan:
            return False
        else:
            return True

    def cenaRegistracije(self):
        if self.kubikaza < 2000:
            return (self.kubikaza*100)
        else:
            return (self.kubikaza*100)*130//100
