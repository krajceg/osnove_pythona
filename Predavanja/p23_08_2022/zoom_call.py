from korisnik import Korisnik


class ZoomCall:
    def __init__(self, link: str, password, korisnikHost: Korisnik, korisnikGuest: Korisnik = None):
        if isinstance(link, str):
            self.__link = link
        else:
            raise ValueError("Link mora biti string!")

        self.__password = password

        if isinstance(korisnikHost, Korisnik):
            self.__korisnikHost = korisnikHost
        else:
            raise ValueError("Korisnik mora biti objekat klase Korisnik!")

        if korisnikGuest is None or isinstance(korisnikGuest, Korisnik):
            self.__korisnikGuest = korisnikGuest
        else:
            raise ValueError("Korisnik mora biti objekat klase Korisnik!")

    # Getters:
    def get_link(self):
        return self.__link

    def get_password(self):
        return self.__password

    def get_korisnikHost(self):
        return self.__korisnikHost

    def get_korisnikGuest(self):
        return self.__korisnikGuest

    # Setters:
    def set_korisnikGuest(self, korisnikGuest):
        if isinstance(korisnikGuest, Korisnik):
            self.__korisnikGuest = korisnikGuest
        else:
            return ValueError("Korisnik mora biti objekat klase Korisnik!")

    # Additional methods:
    def pokreniPoziv(self):
        print(f"Zoom Call: {self.__link}")
        print(f"Password: {self.__password}")
        print("Host: ", end="")
        self.__korisnikHost.print()
        print("Guest: ", end="")
        self.__korisnikGuest.print()
        print(
            f"Maximalno trajanje poziva je: {self.__korisnikHost.maxiDuzinaVideoPoziva()}min.")
