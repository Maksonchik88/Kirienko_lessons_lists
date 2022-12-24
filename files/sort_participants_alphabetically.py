file = open("files/check.txt")
d = {}
for line in file:
    a, b, c, e = line.split()
    key = ' '.join([a, b])
    value = int(e)
    if key not in d:
        d[key] = value

x = list(sorted(d))

for el in x:
    print(el, d[el])

file.close()