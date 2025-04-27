# Zadatak
# Napisati program koji ispisuje za uneti broj a da li je deljiv sa 2 i deljiv sa 3.
# Upoznajte se sa opertorom moduo % dok ne dodjemo do tog operatora.

a = int(input("Unesite a: "))

if a % 2 == 0 and a % 3 == 0:
    print("Uneti broj je deljiv sa 2 i 3")

else:
    print("Uneti broj nije deljiv sa 2 i sa 3")
