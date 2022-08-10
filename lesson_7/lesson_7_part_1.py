lst = list(input("Введите список из чисел: "))
index = int(input("Введите индекс элемента из списка выше: "))
for n in range(index, len(lst) - 1):
    lst[n] = lst[n + 1]
    #print(lst)
lst.pop()
print[str(n) for n in lst]
