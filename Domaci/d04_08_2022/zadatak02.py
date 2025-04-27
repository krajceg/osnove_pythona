# Napisati program koji proverava da li je kliknuto u okviru login forme za web stranicu.
# Korisnik unosi x i y koordinate za T1, T2 i M. Ispisati odgovarajuce poruke.
# T1 i T2 su pozicije login forme. M je pozicija na kojoj je kliknuto

# Primer izvrsenja 1:
# Unesite x za T1: 10
# Unesite y za T1: 100
# Unesite x za T2: 100
# Unesite y za T2: 0
# Unestie x za M: 50
# Unesite y za M: 50
# Kliknuto je unutar forme

# Primer izvrsenja 2:
# Unesite x za T1: 10
# Unesite y za T1: 100
# Unesite x za T2: 100
# Unesite y za T2: 0
# Unestie x za M: 120
# Unesite y za M: 50
# Nije kliknuto je unutar forme

xT1 = int(input("Unesite x za T1: "))
yT1 = int(input("Unesite y za T1: "))
xT2 = int(input("Unesite x za T2: "))
yT2 = int(input("Unesite y za T2: "))
xM = int(input("Unesite x za M: "))
yM = int(input("Unesite y za M: "))

# if (xT1 < xM < xT2) or (xT2 < xM < xT1):
#     if (yT1 < yM < yT2) or (yT2 < yM < yT1):
#         print("Kliknuto je unutar forme")

if min(xT1, xT2) < xM < max(xT1, xT2) and min(yT1, yT2) < yM < max(yT1, yT2):
    print("Kliknuto je unutar forme")