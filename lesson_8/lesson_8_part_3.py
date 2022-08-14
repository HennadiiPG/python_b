import random
Matrix = [random.randint(1, 10) for i in range(15)]
print(Matrix)
s = 0 #"четные"
w = 0 # нечетные
for i in Matrix:
    if i % 2 == 0:
        s += i
    elif i % 2 != 0:
        w += i
print(s)
print(w)
if w > s:
    print(True)
else:
    print(False)