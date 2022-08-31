from random import randint


def sort_matrix():
    # выравниваем матрицу
    for i in range(m):
        for j in range(m):
            if matrix[i][j] <= 9:
                print('   {}'.format(matrix[i][j]), end=' ')
            else:
                print('  {}'.format(matrix[i][j]), end=' ')
        print()


def sort_fun():
    # сортируем столбцы по возрастанию сумм
    list_sum = [sum([matrix[index_col][i] for index_col in range(m)]) for i in range(m)]
    flag = True
    while flag:
        flag = False
        for i in range(m - 1):
            j = i + 1
            if list_sum[i] > list_sum[j]:
                list_sum[i], list_sum[j] = list_sum[j], list_sum[i]
                flag = True
                for line in range(m):
                    matrix[line][i], matrix[line][j] = matrix[line][j], matrix[line][i]

    print("После сортировки столбцов по возростанию суммы:")
    sort_matrix()
    print([sum(row[i] for row in matrix) for i in range(len(matrix[0]))], "Сумма столбцов")
    # сортруем элементы столбцов по условию
    for coll in range(m):
        if not coll % 2:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] < matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], matrix[i][coll]
                        flag = True
        else:
            flag = True
            while flag:
                flag = False
                for i in range(m - 1):
                    j = i + 1
                    if matrix[i][coll] > matrix[j][coll]:
                        matrix[i][coll], matrix[j][coll] = matrix[j][coll], matrix[i][coll]
                        flag = True


m = int(input('Введите значение M больше 5: '))
if m > 5:
    print("До сортировки")
    matrix = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
    sort_matrix()
    print([sum(row[i] for row in matrix) for i in range(len(matrix[0]))], "Сумма столбцов")
    print()
    sort_fun()
    print()
    print("После окончательной сортировки")
    sort_matrix()
    print([sum(row[i] for row in matrix) for i in range(len(matrix[0]))], "Сумма столбцов")

else:
    print("Ввели значение меньше 5")