file = open("check.txt")
d = {}
for line in file:
    if line != '':
        k, v = line.split()[2:]
        if k not in d:
            d[k] = [v]
        else:
            d[k].append(v)
d = dict(sorted(d.items()))
for val in d.values():
    a = list(map(int, val))
    b = sum(a)/len(a)
    print(b, end=' ')

file.close()
