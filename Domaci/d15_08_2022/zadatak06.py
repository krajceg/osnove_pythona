# (Za vezbanje )Napisati funkciju koja za pronalazi koliko ima celih brojeve izmedju brojeva M i N.

# Primer izvrsenja:
# izbroji(5, 10) ima za rezultat 4. Kako? 5 6 7 8 9 10
# izbroji(-5, 1) ima za rezultlat 5 . Kako? -5 -4 -3 -2 -1 0 1
# Napomena: Resiti bez koriscenja petlji.

def brojCelihBrojeva(m, n):
    brojCelih = (abs(m-n)-1)
    return brojCelih


a = 5
b = 10
c = brojCelihBrojeva(a, b)
print(f"izbroj({a}, {b}) ima za razultat {c}")
