lst = input("Введите список из чисел: ").split()
lst_1 = input("Введите ещё один список из чисел: ").split()
lst.extend(lst_1)
lst_2 = []
for i in lst:
    if i not in lst_2:
        lst_2.append(i)
print("Количество уникальных чисел в первом и втором списке = ", len(lst_2))
