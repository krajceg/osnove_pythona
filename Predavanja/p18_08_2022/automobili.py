class auto():
    def __init__(self, imeIPrezime=None, markaAutomobila=None, brojVrata=None, potrosnja=None, maxBrzine=None,
                 trenutnaBrzina=None, godinaProizvodnje=None, mesecDoKadJeRegistrovan=None, kubikaza=None, brojRegistracije=None,
                 daLiJeKlimaUkljucena=None, kapacitetGoriva=None, trenutnaKolicinaGoriva=None):
        self.imeIPrezime = imeIPrezime
        self.markaAutomobila = markaAutomobila
        self.brojVrata = brojVrata
        self.potrosnja = potrosnja
        self.maxBrzine = maxBrzine
        self.trenutnaBrzina = trenutnaBrzina
        self.godinaProizvodnje = godinaProizvodnje
        self.mesecDoKadJeRegistrovan = mesecDoKadJeRegistrovan
        self.kubikaza = kubikaza
        self.brojRegistracije = brojRegistracije
        self.daLiJeKlimaUkljucena = daLiJeKlimaUkljucena
        self.kapacitetGoriva = kapacitetGoriva
        self.trenutnaKolicinaGoriva = trenutnaKolicinaGoriva

    def stampaj(self):
        print(self.imeIPrezime)
        print(f"{self.markaAutomobila} - {self.brojVrata}-ro vrata")
        print(f"Registracija: {self.brojRegistracije}")
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
            return True
        else:
            return False

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

    def dodajGas(self):
        self.trenutnaBrzina = self.trenutnaBrzina + 10
        if self.trenutnaBrzina > self.maxBrzine:
            self.trenutnaBrzina = self.maxBrzine

    def koci(self):
        self.trenutnaBrzina = self.trenutnaBrzina - 10
        if self.trenutnaBrzina < 0:
            self.trenutnaBrzina = 0

    def trenutnaPotrosnjAuta(self):
        if self.daLiJeKlimaUkljucena == False:
            faktorKlime = 1
        else:
            faktorKlime = 1.2
        return ((self.trenutnaBrzina / 100 * self.potrosnja)*faktorKlime)

    def stampajTablu(self):
        crtice = int((self.trenutnaBrzina*100)/self.maxBrzine)
        for i in range(crtice):
            print("|", end="")
        for i in range(100-crtice):
            print(".", end="")
        print(f" {self.trenutnaBrzina}/{self.maxBrzine}km/h")

    def natociGorivo(self, natocenoGorivo):

        if natocenoGorivo + self.trenutnaKolicinaGoriva > self.kapacitetGoriva:
            natocenoGorivo = self.kapacitetGoriva - self.trenutnaKolicinaGoriva
        self.trenutnaKolicinaGoriva = self.trenutnaKolicinaGoriva + natocenoGorivo
        return natocenoGorivo*170
