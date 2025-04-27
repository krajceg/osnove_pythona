class facebookPost:
    def __init__(self, imeIPrezimeObjavio=None, imeIprezimeNaProfilu=None, tekstObjave=None, brojLajkova=None, brojDeljenja=None):
        self.imeIPrezimeObjavio = imeIPrezimeObjavio
        self.imeIprezimeNaProfilu = imeIprezimeNaProfilu
        self.tekstObjave = tekstObjave
        self.brojLajkova = brojLajkova
        self.brojDeljenja = brojDeljenja

    def like(self):
        self.brojLajkova += 1

    def dislike(self):
        self.brojLajkova -= 1
        if self.brojLajkova < 0:
            self.brojLajkova = 0

    def share(self):
        self.brojDeljenja += 1

    def print(self):
        print(f"{self.imeIPrezimeObjavio} >>> {self.imeIprezimeNaProfilu}")
        print(self.tekstObjave)
        print(f"Likes {self.brojLajkova} | Shares {self.brojDeljenja}")
