from random import randint

m = int(input('Введите значение M: '))
n = int(input('Введите значение N: '))
matrix = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
for c in matrix:
    k = 0
    for i in c:
        k += i
    for j in range(n):
        if c[j] <= 9:
            print("   {}".format(c[j]), end=' ')
        else:
            print("  {}".format(c[j]), end=' ')
    print("    {}".format(k), end=' ')
    print()
for i in range(n):
    print("  ", end='')
print()
for i in range(n):
    k = 0
    for j in range(m):
        k += matrix[j][i]
    print("  {}".format(k), end='')
print()
