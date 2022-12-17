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
# print(d)
# print(lst)
for el in lst:
    a = el[1]
    b = max(a)
    counter = 0
    for j in a:
        if j == b:
            counter += 1
    print(counter, end=' ')

file.close()