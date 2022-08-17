txt = 'pythonist'
txt_1 = list(txt)
d = dict.fromkeys(txt_1, 0)
for i in d:
    d[i] = txt_1.count(i)
print(d)