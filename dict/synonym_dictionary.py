file = open('dict/text.txt')
garbage = file.readline()
data = {}
for line in file:
    line = line.split()
    if len(line) > 1:
        word, synonym = line
        if synonym not in data:
            data[synonym] = word
    else:
        check = ' '.join(line)

print(data[check])

