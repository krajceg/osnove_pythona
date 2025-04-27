# Napisati program koji ucitava broj a i ispisuje poruke:
# Ukoliko je broj a do 10 stampamo da je jednocifren broj
# Ukoliko je broj a do 100 stampamo da je dvocifren broj
# Ukoliko je broj a veci od 100 stampamo da je trocifren.
# Napisati program koji ucitava brojeve a, b i c sa tastature i proverava da li je broj a u opsegu od b do c.

a = int(input("Unesite a: "))

if a < 10:
    print("a je jednocifreni broj")
elif a < 100:
    print("a je dvocifren broj")
elif a < 1000:
    print("a je trocifren broj")
else:
    print("a je stvarno veliki broj :D")
