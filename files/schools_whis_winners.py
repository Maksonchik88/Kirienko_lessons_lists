file = open("files/check.txt")

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

max_key = max(dict_1)

res = sorted(dict_1.get(max_key))

for c in res:
    print(c, end=' ')

file.close()