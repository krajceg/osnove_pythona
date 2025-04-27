# Napisati program koji ucitava stranicu jednakostranicnog trougla sa tastature
# i ispisuje povrsinu i obim trougla. Koren iz tri neka bude konstanta 1.73
# Primer izvrsenja programa:
# Unesite stranicu trougla: 10
# Povrsina je 43.25
# Obim je 30

a = int(input("Unesite stranicu jednakostranicnog trougla: "))

obim = 3 * a
povrsina = (a * a * 1.73) / 4

print(f"Povrsina je: {povrsina}")
print(f"Obim je: {obim}")
