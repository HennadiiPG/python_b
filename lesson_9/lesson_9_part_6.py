inp_str = """Любіть Україну, як сонце любіть,
            як вітер, і трави, і води...
            В годину щасливу і в радості мить,
            любіть у годину негоди.
            Любіть Україну у сні й наяву,
            вишневу свою Україну,
            красу її, вічно живу і нову,
            і мову її солов'їну.
            Без неї — ніщо ми, як порох і дим,
            розвіяний в полі вітрами...
            Любіть Україну всім серцем своїм
            і всіми своїми ділами."""

print(inp_str)
e = ",", ".", "—", "...", "'",
for i in range(len(e)):
    inp_str = inp_str.replace(e[i], "")
a = inp_str.split()
d = dict.fromkeys(a, 0)
for i in d:
     d[i] = a.count(i)

d_max = max(d, key=d.get)
d_min = min(d, key=d.get)

d_max_1 = [k for k in d if d[k] == d[d_max]]
print("Слово '", d_max_1, "' больше всего встречается в тексте: ", d[d_max], "раз" )

d_min_1 = [k for k in d if d[k] == d[d_min]]
print("Слова '", d_min_1, "' меньше всего встречаются в тексте: ", d[d_min], "раз")
