# Za klasu Tacka, koja ima privatne atribute:
# x - x koordinata
# y - y koordinata
# Javne metode:
# metodu stampaj
# imamo difoltni konstruktor
# imamo konstuktor koji prima obe koordinate za kreiranje objekta
# geter za x
# geter za y
# seter za x
# seter za y

# U glavnom programu kreirati dva objekta:
# Jedan preko difoltnog konstuktora i postavite koordinate na 10 i 20
# Drugi objekat preko konsuktora sa parametrima i postavite kooridnate na 30 i 40


from Tacke import tacka

tacka1 = tacka()
tacka1.set_x(10)
tacka1.set_y(20)

tacka2 = tacka(30, 40)

tacka1.stampaj()
tacka2.stampaj()
