import random

n = m = int(input("Введите число для вывода матрицы: "))
Matrix = [[random.randint(1, 100) for j in range(n)] for i in range(m)]
for i in range(m):
    print(Matrix[i])