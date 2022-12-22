# from collections import Counter
# file = open('check.txt')
# d = {}
# for line in file:
#     name, surname, school, ball = line.split()
#     key = ' '.join([name, surname])
#     value = school
#     d[key] = int(value)
# values = d.values()
# counter_val = Counter(values)
# counter_val = dict(sorted(counter_val.items(), key=lambda item: item[1]))
#
# print(dict(counter_val))

d = {}

file = open('check.txt')
for line in file:
    school, ball = list(map(int, line.split()[-2:]))
    if school in d:
        d[school][0] += 1
        d[school][1] += ball
    else:
        d[school] = [1, ball]

max_mem = max(d.items(), key=lambda x: x[1][0])[1][0]
filtr_max_mem = list(filter(lambda x: x[1][0] == max_mem, d.items()))

print(max_mem)
d_list = sorted(d.items(), reverse=False)
print(d_list)
for i in d_list:
    for j in i[1]:
        if j == max_mem:
            print(i[0], end=' ')
