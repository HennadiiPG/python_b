lst = input("Введите список из чисел: ").split()
lst_1 = input("Введите ещё один список из чисел: ").split()
lst_2 = []
for i in lst:
    if i not in lst_1:
        lst_2.append(i)
for i in lst_1:
    if i not in lst:
        lst_2.append(i)
print("Количество уникальных чисел в первом и втором списке = ", len(lst_2))
