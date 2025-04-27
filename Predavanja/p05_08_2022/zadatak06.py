# Napisati program koji ispisuje SAMO PARNE brojeve od 1 do 100


for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=", ")
