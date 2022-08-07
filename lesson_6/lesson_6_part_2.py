string = input("Введите строку: ")
char = input("Введите символ: ")
start = -1
count = 0

while True:
    start = string.find(char,  start + 1)
    if start == -1:
        break
    count += 1
print("Количество символов -",  char,  "- в строке =", count)
