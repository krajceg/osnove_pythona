# (Za vezbanje)
# Napisati program koji stampa 20 pozicija.
# Za aktivnu poziciju stampa *
# Za neaktivnu pozciju stampa _
# 	Korisnik unosi granice za nekativni opseg, unoseci A i B.
# 	Primer izvrsenja:
# 	Unesite a: 5
# 	Unesite b: 10
#             * * * * _ _ _ _ _ _ * * * * * * * * * *
# 	Objasnjenje: stampamo _ od 5 do 10 u ostalim situacijama stampamo *

a = int(input("Unesite a: "))
b = int(input("Unesite b: "))

for i in range(1, 21):
    if a <= i <= b:
        print("_", end=" ")
    else:
        print("*", end=" ")
