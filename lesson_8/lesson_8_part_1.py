n = int(input("Введите число для вывода матрицы: "))
b = [[i * -1 if j % 2 != 0 else j for i in range(n, 0, -1)] for j in range(n)]
for a in b:
    print(a)
