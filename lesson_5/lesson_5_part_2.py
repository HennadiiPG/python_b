n = int(input("Введите число:"))
for k in range(n + 1):
  count = 0
  p = k
  while p > 0:
    p //= 10
    count += 1
  i = k ** 2
  z = 10 ** count
  h = i % z
  if k == h:
    print(k)