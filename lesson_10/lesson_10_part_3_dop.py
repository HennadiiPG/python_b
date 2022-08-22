planetarium = set(range(1, 20))
circus = set(range(21, 31))
stadium = set(range(32, 38))
home = 3
planetarium_circus = set(range(1, 6))
planetarium_stadium = set(range(7, 10))
circus_stadium = {10}
a = len((planetarium | circus | stadium) - (planetarium_stadium | planetarium_circus | circus_stadium)) + home
print(a, "учеников в классе")