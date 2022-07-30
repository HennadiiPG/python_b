
years = int(input("Пожалуйста, введите год:"))

if 1900 < years < 1_000_000:
    print()
else:
    if years % 4 == 0 and years % 100 != 0:
        print(years, "год високосный")
    elif years % 400 == 0:
        print(years, "год високосный")
    else:
        print(years, "год не високосный")
