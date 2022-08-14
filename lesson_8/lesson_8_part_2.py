import random
n = int(input("Введите число для вывода матрицы: "))
Matrix = [[random.randint(1, 10) for i in range(n)] for j in range(n)]
for i in range(n):
    print(Matrix[i])
a = [Matrix[i][j] for j in range(n) for i in range(n) if i == j]
print("Сумма чисел диагонали матрицы = ", sum(a))
w = sum(row[-1] for row in Matrix)
print("Сумма чисел последнего столбца матрицы = ", w)