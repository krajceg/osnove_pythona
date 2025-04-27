class smartAirConditioning:
    def __init__(self, markaKlime=None, potrosnjaDokHladi=None, potrosnjaDokGreje=None, temperatura=None, mod=None):
        self.markaKlime = markaKlime
        self.potrosnjaDokHladi = potrosnjaDokHladi
        self.potrosnjaDokGreje = potrosnjaDokGreje
        if temperatura is not None:
            self.temperatura = max(16, min(temperatura, 35))
        else:
            self.temperatura = 16
        self.mod = mod

    def stampaj(self):
        print(f"Marka klime: {self.markaKlime}")
        print(f"Potrosnja dok hladi: {self.potrosnjaDokHladi} kW/h")
        print(f"Potrosnja dok greje: {self.potrosnjaDokGreje} kW/h")
        print(f"Trenutna temperatura: {self.temperatura}c")
        print(f"Aktivan mod: {self.mod}")

    def racunaMesecnuPotrosnju(self):
        if self.mod == "hladi":
            return 30*15*self.potrosnjaDokHladi
        elif self.mod == "greje":
            return 30*15*self.potrosnjaDokGreje
        else:
            print("Mod nije validan")

    def racunaKolikoNovcaPotrosi(self):
        zelenaZona = 350 * 6
        plavaZona = (self.racunaMesecnuPotrosnju()-350)*9
        return zelenaZona + plavaZona
