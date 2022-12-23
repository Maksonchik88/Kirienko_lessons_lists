d = {}

file = open('check.txt')
for line in file:
    school, ball = list(map(int, line.split()[-2:]))
    if d.get(school, None):
        d[school] += 1
    else:
        d[school] = 1

min_score = 100
for c in d.values():
    if c < min_score:
        min_score = c

d2 = {}
for k, v in d.items():
    if v not in d2:
        d2[v] = [k]
    else:
        d2[v].append(k)

print(*sorted(d2[min(d2)]))


file.close()