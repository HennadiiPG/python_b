lst = [int(s) for s in input("Введите список из чисел: ").split()]
k = int(input("Введите индекс элемента из списка выше (k): "))
с = int(input("Введите число которое хотите добавить в список (C): "))
lst.append(0)
for i in range(len(lst) - 1, k, -1):
    lst[i] = lst[i-1]
lst[k] = с

print(' '.join([str(i) for i in lst]))
