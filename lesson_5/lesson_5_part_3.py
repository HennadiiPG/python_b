n = int(input("Введите число:"))
sum = kol = double_numbers = not_paired_numbers = maximum = 0
minimum = n
while n != 0:
    sum += n
    kol += 1
    if n % 2 == 0:
        double_numbers += 1
    else:
        not_paired_numbers += 1
    if n > maximum:
        maximum = n
    elif n < minimum:
        minimum = n

    n = int(input("Введите число:"))
print("Сумма введенных чисел:", sum)
print("Среднее арифметическое введенных чисел:", sum / kol)
print("Количество парных чисел:", double_numbers)
print("Количество не парных чисел", not_paired_numbers)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)