file = open("files/check.txt")

d = {}

for line in file:
    school, ball = line.split()[2:]
    school, ball = int(school), int(ball)
    if school not in d:
        d[school] = 0
        d[school] = 1
    else:
        d[school] += 1
print(d)
d1 = {}
d2 = {}
for k, v in d.items():
    if v == 1:
        d1[k] = v
    elif v > 1:
        d2[k] = v

d2 = dict(sorted(d2.items()))
d1 = list(sorted(d1.keys()))
d2 = list(d2.keys())
print(*d2, *d1)
