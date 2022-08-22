newspaper = set(range(1, 76))
journal = set(range(76 - 13, (76 - 13) + 27))
n_families = newspaper | journal
print(len(n_families), "семей живут в доме N")
