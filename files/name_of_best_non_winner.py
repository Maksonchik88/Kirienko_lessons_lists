file = open("check.txt")
d = {}
for line in file:
    a, b, c, e = line.split()
    key, value = int(e), ' '.join(([a, b]))
    if int(key) not in d:
        d[key] = [value]
    else:
        d[key].append(value)
print(d)
max_val = 0
pre_max = 0
for num in d.keys():
    if int(num) > max_val:
        pre_max = max_val
        max_val = num
    elif num > pre_max:
        pre_max = num
print(max_val, pre_max)
c = [d.keys()].count(pre_max)
for k, v in d.items():
    if k == pre_max:
        if len(v) == 1:
            print(*v)
        else:
            print(len(v))


