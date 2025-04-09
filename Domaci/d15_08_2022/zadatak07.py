# (Za vezbanje)Napisati funkciju koja za tri prosledjena broja vraca najmanji od ta 3.
# U glavnom programu iskoristi funkciju i ispisti odgovarajucu poruku.

def najmanjiBroj(a, b, c):
    nbr = a
    if nbr > b:
        nbr = b
    if nbr > c:
        nbr = c

    return nbr


a = 14
b = 2
c = 99

d = najmanjiBroj(a, b, c)
print(f"Najmanji broj izmedju {a}, {b} i {c} je {d}")
