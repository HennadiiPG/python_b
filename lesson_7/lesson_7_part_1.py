lst = [int(s) for s in input("Введите список из чисел: ").split()]
k = int(input("Введите индекс элемента из списка выше: "))
for i in range(k + 1, len(lst)):
    lst[i - 1] = lst[i]
lst.pop()
print(' '.join([str(i) for i in lst]))
