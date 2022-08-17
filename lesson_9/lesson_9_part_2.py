import random
my_dict = {i: random.randint(1, 10) for i in range(1, 21)}
print(my_dict)

result = 1
for value in my_dict:
    result = result * my_dict[value]
print("Результат умножения числовых значиний словаря = ", result)