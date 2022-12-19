file = open("/home/max/projects/kirienko/files/check.txt")
d = {}
for line in file:
    a, b, c, e = line.split()
    name = ' '.join([a, b])
    ball = e
    d[name] = int(ball)
valu = []
for value in d.values():
    valu.append(int(value))
temp = sorted(valu) # [91, 92, 93, 93]
maks = int(temp[-1])
while maks in temp:
    temp.remove(maks)
gen = max(temp)
counter = temp.count(gen)
if counter == 1:
    for k, v in d.items():
        if gen == v:
            print(k)
else:
    print(counter)