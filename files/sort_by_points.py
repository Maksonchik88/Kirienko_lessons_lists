file = open("/home/max/projects/kirienko/files/check.txt")
d = {}

for line in file:
    a, b, c, e = line.split()
    key = int(e)
    value = ' '.join([a, b])
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

x = sorted(d, reverse=True)

for el in x:
    for k, v in d.items():
        if el == k:
            if len(v) == 1:
                print(*v, k, end=' ')
                print()
            elif len(v) > 1:
                v.sort()
                print(v[0], k, end=' ')
                print()
                print(v[1], k, end=' ')
                print()

file.close()