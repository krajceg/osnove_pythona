from video import Video
import math


class YoutubePlayer:
    def __init__(self, video: Video = None, kvalitetVidea: int = 144, rezim: str = "Mini Player", jacinaZvuka: int = 75, trenutnoVreme: int = 0):
        if video is None or isinstance(video, Video):
            self.__video = video
        else:
            raise ValueError("Video mora biti objekat klase Video!")

        if isinstance(kvalitetVidea, int):
            self.__kvalitetVidea = kvalitetVidea
        else:
            raise ValueError("Kvalitet videa mora biti intiger!")

        if isinstance(rezim, str):
            self.__rezim = rezim
        else:
            raise ValueError("Rezim mora biti string!")

        if isinstance(jacinaZvuka, int):
            self.__jacinaZvuka = jacinaZvuka

        else:
            raise ValueError("Jacina zvuka mora biti intiger!")

        if isinstance(trenutnoVreme, int):
            self.__trenutnoVreme = trenutnoVreme

        else:
            raise ValueError("Trenutno vreme mora biti ingiger")

    # Getters:

    def get_video(self):
        return self.__video

    def get_kvalitetVidea(self):
        return self.__kvalitetVidea

    def get_rezim(self):
        return self.__rezim

    def get_jacinaZvuka(self):
        return self.__jacinaZvuka

    def get_trenutnoVreme(self):
        return self.__trenutnoVreme

    # Additional methods:

    def ucitajVideo(self, video: Video):
        self.__video = video
        self.__trenutnoVreme = 0
        self.__video.pogledaj()

    def pojacaj(self):
        self.__jacinaZvuka = min(self.__jacinaZvuka + 10, 100)

    def smanji(self):
        self.__jacinaZvuka = max(self.__jacinaZvuka - 10, 0)

    def postaviKvalitet(self, brzinaInterneta):
        if brzinaInterneta <= 2:
            self.__kvalitetVidea = 144
        elif brzinaInterneta <= 4:
            self.__kvalitetVidea = 240
        elif brzinaInterneta <= 6:
            self.__kvalitetVidea = 360
        elif brzinaInterneta <= 8:
            self.__kvalitetVidea = 720
        else:
            self.__kvalitetVidea = 1080

    def aktivirajMiniPlayerMod(self):
        self.__rezim = "Mini Player"

    def aktivirajBioskopskiMod(self):
        self.__rezim = "Bioskopski rezim"

    def aktivirajPrekoCelogEktranaMod(self):
        self.__rezim = "Preko celog ekrana"

    def premotajUnapred(self):
        self.__trenutnoVreme = min(
            self.__trenutnoVreme + 10, self.__video.get_duzinaVidea())

    def premotajUnazad(self):
        self.__trenutnoVreme = max(self.__trenutnoVreme - 10, 0)

    def iscrtajZvuk(self):
        if self.__jacinaZvuka == 0:
            print("</")
        else:
            print("<: ", end="")
            print("|" * (math.floor(self.__jacinaZvuka / 10)))

    def iscrtajRezim(self):
        if self.__rezim == "Mini Player":
            print("[]")
        elif self.__rezim == "Bioskopski rezim":
            print("[..]")
        else:
            print("[||||]")

    def iscrtajTrenutnoVreme(self):
        trenutnoVremeMinuti = math.floor(self.__trenutnoVreme/60)
        trenutnoVremeSekunde = self.__trenutnoVreme % 60

        duzinaVideaMinuti = math.floor(self.__video.get_duzinaVidea() / 60)
        duzinaVIdeaSekunde = self.__video.get_duzinaVidea() % 60

        print(
            f"{trenutnoVremeMinuti}:{trenutnoVremeSekunde} / {duzinaVideaMinuti}:{duzinaVIdeaSekunde}", end=" ")

    def iscrtajTimeline(self):
        brojZvezdica = self.__trenutnoVreme * 100 / self.__video.get_duzinaVidea()

        for i in range(100):
            if i < brojZvezdica:
                print("*", end="")
            else:
                print(".", end="")

    def iscitaj(self):
        self.iscrtajTrenutnoVreme()
        self.iscrtajZvuk()
        print("Timeline: ", end="")
        self.iscrtajTimeline()
        print()
        print(f"Kvalitet: {self.__kvalitetVidea}p")
        print(f"Rezim: {self.__rezim}")
        print(self.__video.get_nazivVidea())
        print(
            f"Likes {self.__video.get_brojLajkova()} | Dislikes {self.__video.get_brojDislajkova()}")
        print(f"{self.__video.get_brojPregleda()} Pregleda")

    def sherovanjeVidea(self):
        print("".join(["https://youtu.be/", self.__video.get_id()]))
