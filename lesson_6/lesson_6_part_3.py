while True:
    input_number = input("Введите число от 3 до 9: ")
    if not input_number.isnumeric():
        print("Вы ввели не число.")
        break
    elif not 3 <= int(input_number) <= 9:
        print("Ваше число не в диапазоне.")
        break
    else:
        i = int(input_number)
        for n in range(1, i + 1):
            for j in range(1, n + 1):
                print(j, end=" ")
            for j in range(n - 1, 0, -1):
                print(j, end=" ")
            print()
        break