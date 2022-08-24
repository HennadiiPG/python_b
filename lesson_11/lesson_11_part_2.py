f = lambda x, y = 2: x ** y
arr = range(1, 16)
arr1 = range(1, 6)
print(f(10))
print(list(map(f, arr)))
print(list(map(f, arr, arr1)))
