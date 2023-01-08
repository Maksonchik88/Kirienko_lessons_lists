data = {}

with open("dict/text.txt") as file:
    for lines in file:
        lines = lines.split()
        for line in lines:
            if line not in data:
                data[line] = 0
                print(data[line], end=' ')
            else:
                data[line] += 1
                print(data[line], end=' ')

            # data[line] = data.get(line, -1)
            # data[line] += 1
            # print(data[line], end=' ')
