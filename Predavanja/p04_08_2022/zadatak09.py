# 9. Zadatak (za vezbanje)
# Napisati program koji simulira ponasanje kontrole za zvuk na jutjubu..
# Kada se ucita video difoltna jacina zvuka je 75.
# Korisnik unosi 5 akcija. Jednu od sledecih:
# pojacaj - pojacava zvuka za 10
# smanji - smanjuje zvuk za 10.
# mute - postavlja zvuk na 0.
# Na kraju programa odstampati jacinu zvuka.
# NAPOMENA: Jacina zvuka nikad ne moze da ode iznad 100 niti da padne ispod 0.

# Primer izvrsenja:
# Unesite akciju: pojacaj (objasnjenj: nakon ovoga je 85)
# Unesit akciju: pojacaj (objasnjenje: nakon ovoga je 95)
# Unesite akciju: pojacaj (objasnjeje: nakon ovoga je 100, jer ne moze da bude 105)
# Unesit akciju: mute (ovjasnjenje: nakon ovoga je 0)
# Unesit akciju: smanji (objasnjenje: nakon ovoga ostaje 0)
# Jacina zvuka je 0.

jacinaZvuka = 75

for i in range(5):
    akcija = str(input("Unesite zeljenu akciju: "))
    if akcija == "pojacaj":
        jacinaZvuka += 10
        if jacinaZvuka > 100:
            jacinaZvuka = 100
    elif akcija == "smanji":
        jacinaZvuka -= 10
        if jacinaZvuka < 0:
            jacinaZvuka = 0
    elif akcija == "mute":
        jacinaZvuka = 0

print(f"Jacina zvuka je: {jacinaZvuka}")
