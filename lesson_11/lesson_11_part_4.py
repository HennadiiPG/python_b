
def spreadsheet(foo):

    def wrapper(*args, **kwargs):
        k = foo(*args, **kwargs)
        p = list(k)
        p.sort()
        print(" ", "_" * len(str(p[-1])), " ", "_" * 12, " ", "_" * 9)
        for i in range(len(p)):
            print("|", str(p[i]).ljust(len(str(p[-1])), " "), "|", "Кратное 3".ljust(12, " ") if p[i] % 3 == 0
                  else "Не кратное 3".rjust(12, " "),
                  "|", "Парное".ljust(9, " ") if p[i] % 2 == 0 else "Не парное".ljust(9, " "), "|")
            print("|", "_" * len(str(p[-1])), "|", "_" * 12, "|", "_" * 9, "|")
    return wrapper


@spreadsheet
def table_values(x):
    import random
    n = set(random.randint(1, 100) for _ in range(1, x+1))
    return n


table_values(7)
