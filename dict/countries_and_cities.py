file = open("dict/text.txt")
data = {}
num = int(file.readline())

for _ in range(num):
    line = file.readline()
    line = line.split()
    country = line[0]
    cities = line[1:]
    if country not in data:
        data[country] = cities
num_2 = int(file.readline())

for _ in range(num_2):
    line = file.readline().rstrip()
    for country, cities in data.items():
        if line in cities:
            print(country)