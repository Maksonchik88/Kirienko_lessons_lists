file = open("dict/text.txt")
lines = file.readlines()

file.close()

data = {}
for line in lines:
    line = line.split()
    for word in line:
        if word not in data:
            data[word] = 0
        data[word] += 1

data_sort = sorted(data.items(), key=lambda x: (-x[1], x[0]))

for word, count in data_sort:
    print(word)