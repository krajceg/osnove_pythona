# Zadatak
# Napisati metodu koja vrsi konverziju rimske(string) u arapske brojeve(int).
# 1 - I
# 2 - II
# 3 - III
# 4 - IV
# 5 - V
# Kao parametar se unosi vrednost rimkog broja(string) a vraca se arapski (int).
# Ako se unese V vraca se 5.

def rimskiUArapski(rimski):
    if rimski == "I":
        return 1
    elif rimski == "II":
        return 2
    elif rimski == "III":
        return 3
    elif rimski == "IV":
        return 4
    elif rimski == "V":
        return 5


rimskiBroj = "III"
arapskiBroj = rimskiUArapski(rimskiBroj)
print(arapskiBroj)
