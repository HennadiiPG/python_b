"""Модуль сортування.

В модулі представлені функції сортування які були написані під час виконання
домашніх завданнь впродож вивчення курсу Python Basic до 13 уроку.

    1. Функція генератор простих чисел у дипазоні заданих двома аргументами.

    2. Функція перевірки суми двух чисел на еквівалентність числу переданому
       2-м параметром. Повертає булеве значення як результат пошуку фукції.

    3. Функція виводу чисел у вигляді таблиці у відсортированому
       порядку, де до кожного числа є коментар - чи число кратне 3 чи ні,
       і чи парне число чи ні.

"""


def prost_chusla(x, y):
    """
    :param x: Аргумент функції №1
    :param y: Аргумент функції №2
    :return: Виводить результат роботи генератора

    Функцію генератор простих чисел у дипазоні заданих двома аргументами.
    """
    for number in range(x, y + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number


def ekviv_sum_pervogo_chusla(x, y):
    """
    :param x: Список або генератор виразу
    :param y: Число
    :return: Повертає булеве значення як результат пошуку фукції.

    Функцію приймає на вхід параметри: список (або генератор виразу)
    чисел будь-якої довжини та число.
    Функція перевіряє чи є у списку 2 числа сума яких еквівалентна числу
    переданому 2-м параметром. Функція повертає булеве значення як результат
    пошуку фукції.
    """
    summa = False
    for i in range(1, x + 1):
        for n in range(1, x + 1):
            if i + n == y:
                summa = True
                # print(i, n)
            break
    return summa


def sort_parn_krat_3(x, y):
    """
    :param x: Початкове значення списку
    :param y: Кінцеве значення списку
    :return: Повертає відсортирований список

    Функція виводить числа із списку у вигляді таблиці у відсортированому
    порядку. Де до кожного числа є коментар - чи число кратне 3 чи ні,
    і чи парне число чи ні
    """
    p = range(x, y + 1)
    print(" ", "_" * len(str(p[-1])), " ", "_" * 12, " ", "_" * 9)
    for i in range(len(p)):
        print("|", str(p[i]).ljust(len(str(p[-1])), " "),
              "|", "Кратное 3".ljust(12, " ") if p[i] % 3 == 0
              else "Не кратное 3".rjust(12, " "),
              "|", "Парное".ljust(9, " ") if p[i] % 2 == 0
              else "Не парное".ljust(9, " "), "|")
        print("|", "_" * len(str(p[-1])), "|", "_" * 12, "|", "_" * 9, "|")

    return sort_parn_krat_3


__all__ = ["prost_chusla", "ekviv_sum_pervogo_chusla", "sort_parn_krat_3"]

if __name__ == '__main__':
    pass
