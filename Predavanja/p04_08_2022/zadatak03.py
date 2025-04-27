# Napisati program koji ucitava brojeve a, b i c sa tastature i proverava da li je broj a u opsegu od b do c.

# ………b=0……………a=22…………………c=50…………

a = int(input("Unesite a: "))
b = int(input("Unesite b: "))
c = int(input("Unesite c: "))

if a > b and a < c:
    print("a je u opsegu b i c")
