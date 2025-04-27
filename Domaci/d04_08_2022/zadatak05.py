# Napisati program koji u zavisnosti od operatora koji unosi korisnik sa tastature
# (operator je string i moze imati vrednosti + , - , *, /) racuna  i ispisuje na ekranu odgovarajuci zbir,
# razliku, proizvod ili kolicnik za dva broja a i b uneta sa tastature.

a = int(input("Uneti vrednost a: "))
b = int(input("Uneti vrednost b: "))
operatorS = str(input("Uneti operator: "))


if operatorS == "+":
    c = a + b
elif operatorS == "-":
    c = a - b
elif operatorS == "*":
    c = a * b
else:
    c = a / b

print(f"Rezultat: {c}")
