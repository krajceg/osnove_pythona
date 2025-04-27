# (Za vezbanje)Napisati program koji ucitava 4 broja (a,b,c,d) i
# formira string p (p ima startni deo #)
# tako sto negativne brojeve lepi sa leve strane a pozitivne i nulu sa desne. Konkatanacija stringova u javi-> Koristan link

# Primer izvrsenja 1:
# Unesite a: 10  -> # 10
# Unesite b: -2   -> -2 # 10
# Unesite c: -1   -> -1 -2 # 10
# Unesite d: 9    -> -1 -2 # 10 9
# String p ime vrednost = -1 -2 # 10 9

a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))
c = int(input("Unesite broj c: "))
d = int(input("Unesite broj d: "))
p = "#"

p = p + str(a) if a >= 0 else str(a) + p
p = p + str(b) if b >= 0 else str(b) + p
p = p + str(c) if c >= 0 else str(c) + p
p = p + str(d) if d >= 0 else str(d) + p

print(f"String p ima vrednost: {p}")
