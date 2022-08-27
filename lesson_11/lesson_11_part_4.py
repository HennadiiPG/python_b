
def spreadsheet(foo):

    def wrapper(*args, **kwargs):
        k = foo(*args, **kwargs)
        k = list(k)
        k.sort()
        print(" ", "_" * len(str(k[-1])), " ", "_" * 12, " ", "_" * 9)
        for i in range(len(k)):
            print("|", str(k[i]).ljust(len(str(k[-1])), " "), "|", "Кратное 3".ljust(12, " ") if k[i] % 3 == 0
                  else "Не кратное 3".rjust(12, " "),
                  "|", "Парное".ljust(9, " ") if k[i] % 2 == 0 else "Не парное".ljust(9, " "), "|")
            print("|", "_" * len(str(k[-1])), "|", "_" * 12, "|", "_" * 9, "|")
    return wrapper


@spreadsheet
def table_values(x):
    import random
    x = int(input("dfsdfsdffdfsdfd"))
    n = set(random.randint(1, 10) for i in range(x))
    return n


table_values(5)


