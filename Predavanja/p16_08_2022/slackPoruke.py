class slackMessage():
    def __init__(self, tekstPoruke, imeIPrezime, datumIVreme):
        self.tekstPoruke = tekstPoruke
        self.imeIPrezime = imeIPrezime
        self.datumIVreme = datumIVreme

    def stampaj(self):
        print(f"{self.imeIPrezime} - {self.datumIVreme}")
        print(self.tekstPoruke)
        print()
