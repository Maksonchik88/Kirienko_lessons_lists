file = open("files/check.txt")

d = {}

for line in file:
    key, value = line.split()[2:]
    if key not in d:
        d[key] = [int(value)]
    else:
        d[key].append(int(value))

total = 0
numb_of_parth = 0
sep_by_schools = []

for val in d.values():
    numb_of_parth += len(val)
    total += sum(val)

gpa_schools = total / numb_of_parth

lst = []
for k, v in d.items():
    if (sum(v) / len(v)) > gpa_schools:
        lst.append(int(k))

lst.sort()
print(*lst)


file.close()