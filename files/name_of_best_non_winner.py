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

if len(d[pre_max]) == 1:
    print(*d[pre_max])
else:
    print(len(d[pre_max]))

file.close()


