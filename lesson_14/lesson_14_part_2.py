def dict_handler(d, key, default_value):
    try:
        type(d[key]) == list, dict
    except TypeError as e:
        print(f"Дивись, маємо виняток, введений ключ має змінюваний "
              f"тип данних {e}")
    except KeyError as k:
        print(f"Дивись, маємо виняток, ключа _{k}_ не має в словнику,"
              f" створюєм нову пару в словнику")
        d[key] = default_value
        print(d)
    else:
        print("Отримуем значення по ключу: ", d[key])
    finally:
        print("Блок finally")


if __name__ == '__main__':
    pass


dict_handler({1: "one", 2: "two"}, {1: "one"}, [1, 2, 3])
dict_handler({1: "one", 2: "two"}, [5, 6, 7], [1, 2, 3])
dict_handler({1: "one", 2: "two"}, "three", [1, 2, 3])
dict_handler({1: "one", 2: "two"}, 8, [1, 2, 3])
dict_handler({1: "one", 2: "two"}, 2, [1, 2, 3])