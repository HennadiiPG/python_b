n = int(input("Введите число:"))
result = "НЕТ"
while n > 0:
  p1 = n % 10
  k = n // 10
  n = n // 10
  while k > 0:
    p2 = k % 10
    k = k // 10
    if p1 == p2:
      result = "ДА"
print(result)