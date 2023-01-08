data = {}

with open("dict/text.txt") as file:
    for lines in file:
        lines = lines.split()
        for line in lines:
            data[line] = data.get(line, -1)
            data[line] += 1
            print(data[line], end=' ')
