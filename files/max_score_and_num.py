file = open("/home/max/projects/kirienko/files/check.txt")
lst = []
for line in file:
    line = line.split()
    lst.append(int(line[3]))
print(lst)
max_val = 0
pre_max = 0
for el in lst:
    if el > max_val:
        pre_max = max_val
        max_val = el
    elif el > pre_max:
        pre_max = el
counter = 0
for i in lst:
    if i == pre_max:
        counter += 1
print(pre_max, counter, end=' ')
