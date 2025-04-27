# Napisati program koji za uneti broj x (smatrajte da korisnik unosi jednocifreni broj)
# ispisuje tablicu mnozenja za taj broj.

x = int(input("Unesite broj x: "))

for i in range(1, 10):
    print(f"{x} x {i} = {x*i}")
