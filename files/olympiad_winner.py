file = open('check.txt')
d = {}
for line in file:
    key, value = line.split()[::3]
    if key not in d:
        d[key] = [int(value)]
    else:
        d[key].append(int(value))

# print(d)
max_v = max(d.values())
# print(max(max_v))
lst = []
for k, v in d.items():
    if v == max_v:
        lst.append(k)
if len(lst) == 1:
    print(lst)
else:
    print(len(lst))