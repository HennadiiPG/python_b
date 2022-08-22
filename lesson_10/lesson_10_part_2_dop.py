school = 52
icons = set(range(1, 24))
stamps = set(range(25, 60))
stamps_icons = set(range(1, 17))
collectors = len((icons | stamps) - stamps_icons)
not_collectors = school-collectors
print(not_collectors, "учеников не занимаются коллекционированием")