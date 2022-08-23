def func(x, y):
    summa = False
    for i in range(1, x + 1):
        for n in range(1, x + 1):
            if i + n == y:
                summa = True
                print(i, n)
            break
    return summa


print(func(10, 21))
print(func(12, 10))
