file = open("check.txt")
d = {}
for line in file:
    if line != '':
        k, v = line.split()[2:]
        if int(k) not in d:
            d[int(k)] = [int(v)]
        else:
            d[int(k)].append(int(v))

lst = sorted(d.items())
for val in d.values():
    a = list(map(int, val))
    b = sum(a)/len(a)
    print(b, end=' ')

file.close()
