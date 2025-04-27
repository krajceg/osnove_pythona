# (ZA VEZBANJE) Napisati program koji iscrtava timeline na youtube videu.
# Korisnik unosi duzinu videa u sekundama i trenutno vreme u videu, a program iscrtava timeline
# tako sto deo koji je pogledan iscrtava zvezdicama a ostatak sa crticama.
# Timeline je kontrola koja ima tacno 100 karaktera.
# Primer izvrsenja:
# Unesite duzinu videa (s): 203
# Unesite trenutno vreme videa (s): 20
# (Objasnjenje:Ako video ima 203s a mi smo na 20s, to znaci da je pogledano 9.85% videa (zaokruzicemo to na 9zvezdice ostatak do 100 su crtice)
# *********-------------------------------------------------------------------------------------------

# MOGUCA SU DVA RESENJA:
# Jedno je sa jednom petljom koja u sebi ima if i else
# Drugo je sa 2 petlje, jedna stampa zvezdice a druga stampa crtice

# 	(DOPUNA TAKODJE ZA VEZBANJE)
# Pretvorite vremena u minute i sekune i stavite ih ispod prikaza:
# Primer izvrsenja:
# Unesite duzinu videa (s): 203
# Unesite trenutno vreme videa (s): 20
# (Objasnjenje:Ako video ima 203s a mi smo na 20s, to znaci da je pogledano 9.85% videa (zaokruzicemo to na 9zvezdice ostatak do 100 su crtice)
# *********-------------------------------------------------------------------------------------------
#  0:20 / 3:23

import math

duziznaVidea = int(input("Unesite duzinu videa u sekundama: "))
trenutnoVreme = int(input("Unesite trenutno vreme videa u sekundama: "))

procenatPregledan = math.floor(trenutnoVreme/duziznaVidea*100)

for i in range(100):
    if i < procenatPregledan:
        print("*", end="")
    else:
        print("_", end="")

minutiDuzine = math.floor(duziznaVidea / 60)
if minutiDuzine > 0:
    duziznaVidea = duziznaVidea % 60

minutiTrenutno = math.floor(trenutnoVreme / 60)
if minutiTrenutno > 0:
    trenutnoVreme = trenutnoVreme % 60

print()
print(f"{minutiTrenutno}:{trenutnoVreme} / {minutiDuzine}:{duziznaVidea}")
