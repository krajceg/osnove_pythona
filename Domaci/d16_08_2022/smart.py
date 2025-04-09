class smartAirConditioning():
    def __init__(self, markaKlime=None, izabranaTemp=None, mod=None):
        self.markaKlime = markaKlime
        self.izabranaTemp = izabranaTemp
        self.mod = mod

    def stampaj(self):
        print(f"Marka klime: {self.markaKlime}")
        print(f"Izabrana temperatura klime: {self.izabranaTemp}")
        print(f"Mod klime: {self.mod}")

    def napoljuVecaTemp(self, spoljnaTemperatura):
        if spoljnaTemperatura > self.izabranaTemp:
            return ("Napolju je veca temperatura")
        else:
            return ("Napolju je manja temperatura")
