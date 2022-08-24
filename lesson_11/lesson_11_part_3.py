def foo(x, y):
    for number in range(x, y + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number


for n in foo(1, 100):
    print(n, end=" ")
