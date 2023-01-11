file = open("dict/text.txt")
data = {}
num = int(file.readline())

for _ in range(num):
    line = file.readline()
    line = line.split()
    country = line[0]
    cities = line[1:]
    for city in cities:
        data[city] = country
print(data)
num_2 = int(file.readline())

for _ in range(num_2):
    line = file.readline().rstrip()
    print(data[line])

file.close()
