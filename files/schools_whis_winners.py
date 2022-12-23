file = open("/home/max/projects/kirienko/files/check.txt")
dict_1 = {}
for line in file:
    school, ball = line.split()[2:]
    key = int(ball)
    value = int(school)
    if key not in dict_1:
        dict_1[key] = [value]
    else:
        if value not in dict_1[key]:
            dict_1[key].append(value)
print(dict_1)
max_key = max(dict_1)
print(max_key)
res = sorted(dict_1.get(max_key))

for c in res:
    print(c, end=' ')

file.close()