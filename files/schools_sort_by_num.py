file = open("files/check.txt")
lines = file.readlines()

file.close()

data = {}
for line in lines:
    _, _, school, ball = line.split()
    school, ball = int(school), int(ball)
    if school not in data:
        data[school] = 0
    data[school] += 1
print(data)
data_revers = sorted(data.items(), key=lambda x: (-x[1], x[0]))
print(data_revers)
for school, _ in data_revers:
    print(school, end=' ')