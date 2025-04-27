# Napisati program koji sabira brojeve vece od nule a da ne predje sumu 100.
# 1 + 2 + 3 + 4 + …

suma = 0
i = 0
while suma + i < 100:
    i += 1
    suma = suma + i
    if suma + i > 100:
        print(i)
    else:
        print(f"{i} + ", end="")
