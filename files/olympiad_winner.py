file = open('check.txt')
d = {}
for line in file:
    a, b, c, e = line.split()
    key = ' '.join([a, b])
    value = int(e)
    if key not in d:
        d[key] = value
    else:
        d[key].append(int(value))
max_v = max(d.values())
lst = []
for k, v in d.items():
    if v == max_v:
        lst.append(k)
if len(lst) == 1:
    print(*lst)
else:
    print(len(lst))
file.close()