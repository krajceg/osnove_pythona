# Metoda prima dva parametra N i karakter za stampu. Metoda stampa N karaktera.
# Ako se za N prosledi 5 i za karakter prosledi npr kosa crta (/) stampa se
# / / / / /
# Napomena: Metoda nista ne vraca.

def stampa(broj, stampa):
    for i in range(0, broj):
        print(stampa, end=" ")


stampa(5, "/")
