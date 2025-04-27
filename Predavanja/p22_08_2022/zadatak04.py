from video import Video
from youtubePlayer import YoutubePlayer

video1 = Video("v6tuOipj5mk", "Aca Lukas - Dijabolik", 194, 50, 20, 1000)
video2 = Video(
    "HTdd8QxifbY", "Freddie Mercury - Living On My Own (1993 Remix Remastered)", 230, 100, 10, 2000)

yt1 = YoutubePlayer()
yt1.ucitajVideo(video1)

yt1.aktivirajBioskopskiMod()
yt1.pojacaj()
yt1.postaviKvalitet(40)
yt1.premotajUnapred()
yt1.iscitaj()
print()

yt1.ucitajVideo(video2)
yt1.aktivirajPrekoCelogEktranaMod()
yt1.postaviKvalitet(4)
yt1.pojacaj()
yt1.pojacaj()
yt1.pojacaj()
yt1.pojacaj()
yt1.iscitaj()
