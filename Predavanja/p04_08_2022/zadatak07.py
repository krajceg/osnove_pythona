# Napisati program koji simulira ponasanje kontrole za zvuk na jutjubu..
# Kada se ucita video difoltna jacina zvuka je 75.
# Korisnik unosi akciju sa tastature. Jednu od sledecih:
# pojacaj - pojacava zvuka za 10
# smanji - smanjuje zvuk za 10.
# mute - postavlja zvuk na 0.
# Na kraju programa odstampati jacinu zvuka
# Primer izvrsenja 1:
# Jacina zvuka je 75.
# Unesite akciju: pojacaj
# Nova jacina zvuka je 85

jacinaZvuka = 75

akcija = str(input("Unesite zeljenu akciju: "))

if akcija == "pojacaj":
    jacinaZvuka += 10
elif akcija == "smanji":
    jacinaZvuka -= 10
elif akcija == "mute":
    jacinaZvuka = 0

print(f"Nova jacina zvuka je: {jacinaZvuka}")
