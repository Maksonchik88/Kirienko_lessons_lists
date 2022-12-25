file = open("files/check.txt")
d = {}

for line in file:
    a, b, _, e = line.split()
    key = int(e)
    value = ' '.join([a, b])
    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

x = sorted(d, reverse=True)

for el in x:
    if len(d[el]) == 1:
        print(*d[el], el)
    else:
        for q in d[el]:
            print(q, el)

file.close()