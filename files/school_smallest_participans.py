d = {}

file = open('check.txt')
for line in file:
    school, ball = list(map(int, line.split()[-2:]))
    if school in d:
        d[school][0] += 1
        d[school][1] += ball
    else:
        d[school] = [1, ball]
print(d) # {14: [2, 131], 23: [1, 74], 3: [2, 155], 27: [1, 68]}
min_score = 100
for c in d.values():
    if c[0] < min_score:
        min_score = c[0]
print(min_score)
d_list = sorted(d.items(), reverse=False)
print(d_list)
for i in d_list:
    for j in i[1]:
        if j == min_score:
            print(i[0], end=' ')

file.close()