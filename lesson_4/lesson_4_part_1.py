
integer = input("Подскажите, сколько вас человек?")
pupils = int(integer)

integer = input("Какое количество яблок у вас есть?")
apples = int(integer)

print("Каждому школьнику достанется по:", apples // pupils, "яблок")
print("В корзине останется:", apples % pupils, "яблок")