# Napisati program koji stampa podatke o kreditnoj kartici u formatu kao na slici.
# Od informacija se pamti broj kartice (16 cifara sa razmacima), mesec i godina do kada vazi kartica,
# kao i ime i prezime vlasnika kartice. Kartica se stampa sa zvezdicama i ne brinite ukoliko neka
# zvezdica mrdne i nije u liniji to ce zavisiti od duzine imena.


brojKartice = "1234 1234 1234 1234"
mesecIGodina = "10/25"
imeIprezime = "Svetolik Kljajic"

print("**************************************")
print("*  Credit Card                       *")
print("*     ****                           *")
print("*     ****                           *")
print(f"*      {brojKartice}           *")
print(f"*                 valid > {mesecIGodina}      *")
print("*                                    *")
print(f"*   {imeIprezime}                 *")
print("**************************************")
