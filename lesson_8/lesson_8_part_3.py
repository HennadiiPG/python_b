import random
Matrix = [random.randint(1, 10) for i in range(15)]
print(Matrix)
a = sum([i for i in Matrix if i % 2 == 0])
b = sum([i for i in Matrix if i % 2 != 0])
c = [print("Да") if a < b else print("Нет")]
