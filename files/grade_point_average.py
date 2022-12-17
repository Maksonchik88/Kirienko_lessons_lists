file = open("check.txt")
d = {'9': [], '10': [], '11': []}
for line in file:
    k, v = line.split()[2:4]
    if k not in d:
        d[k] = [v]
    else:
        d[k].append(v)
for val in d.values():
    a = list(map(int, val))
    b = sum(a)/len(a)
    print(b, end=' ')
file.close()