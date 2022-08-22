school = 40
compl = 10
a = set(range(1, 26))
b = set(range(26, 48))
c = set(range(49, 71))
a_b = set(range(1, 34))
a_c = set(range(1, 33))
b_c = set(range(1, 32))

s1 = len((a | b) - a_b) - compl
s2 = len(b | c) - len(b_c) - compl
s3 = len(c | a) - len(a_c) - compl
s = (len(a) - s1 - s3 - compl) + (len(b) - s1 - s2 - compl) + (len(c) - s2 - s3 - compl)
print(s, "учеников читали только одну книгу")
print(s1 + s2 + s3, "учеников прочитали только 2 книги")
print(school - s - s1 - s2 - s3 - compl, " учеников не прочитали ни одной книги")
