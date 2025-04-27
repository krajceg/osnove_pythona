# Napisati program koji sumira brojeve od 1 do 10 i na kraju programa ispisuje sumu.
# suma = 1 + 2 + 3 + … + 10 (ovo je objasnjenje)
# Primer izvrsenja:
# Suma brojeva od 1 do 10 je 55

suma = 0
for i in range(1, 11):
    suma += i

print(f"Suma brojeva od 1 do 10 je {suma}")
