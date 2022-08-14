import random
s = 0
n = int(input("Введите число для вывода матрицы: "))
Matrix = [[random.randint(1, 10) for i in range(n)] for j in range(n)]
for i in range(n):
    print(Matrix[i])
for i in range(n):
    for j in range(n):
        if i == j:
            s += Matrix[i][j]
print("Сумма чисел по диагонали матрицы = ",  s)

w = sum(row[-1] for row in Matrix)
print("Сумма чисел последнего столбца матрицы = ", w)
