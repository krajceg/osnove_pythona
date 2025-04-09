# Napisati funkciju koja za dva jednocifrena broja koja su ulazni parametri funkcije vraca
# novu vrednost koja se formira kao na primeru. METODA NISTA NE STAMPA.
# ako je prvi broj =2, a drugi =3 vraca novu vrednost 23.
# ako je prvi broj =6, a drugi =2 vraca novu vrednost 62.

def noviBroj(a, b):
    return int(f"{a}{b}")


a = 6
b = 2
c = noviBroj(a, b)
print(c)
