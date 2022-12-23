file = open("/home/max/projects/kirienko/files/check.txt")
d = {}
for line in file:
    a, b, c, e = line.split()
    key = ' '.join([a, b])
    value = int(e)
    if key not in d:
        d[key] = value
print(d)
x = list(sorted(d))
print(x)
for el in x:
    for k, v in d.items():
        if el == k:
            print(k, v)

file.close()