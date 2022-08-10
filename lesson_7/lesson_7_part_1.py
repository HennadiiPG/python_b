lst = input("Введите список из чисел: ").split()
index = int(input("Введите индекс элемента из списка выше: "))
for i in range(index + 1, len(lst)):
    lst[i - 1] = lst[i]
lst.pop()
print(lst)
