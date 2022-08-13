n = int(input("Введите число для вывода матрицы: "))
a1 = [[i for i in range(j, j + n)] for j in range(0, n**2-1, n)]
a2 = [i for i in range(-n, 0)]
for i in range(len(a1)):
    if i % 2 == 0:
        a1[i] = [i for _ in range(n)]
    elif i % 2 != 0:
        a1[i] = a2
for b in a1:
    print(b)