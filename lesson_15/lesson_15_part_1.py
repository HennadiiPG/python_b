file_txt = input('Файл: ')
f = open(file_txt, 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()

if __name__ == '__main__':
    pass
