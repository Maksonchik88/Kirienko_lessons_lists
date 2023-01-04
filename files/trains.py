file = open("files/check.txt")
N = int(file.readline())
lines = file.readlines()

file.close()

data = {}
for line in lines:
    line_for_sort = line.split()
    start_station = int(line_for_sort[-2])
    end_station = int(line_for_sort[-1])
    passenger = ' '.join(line_for_sort[:-2])
    stations = start_station, end_station
    if passenger not in data:
        data[passenger] = []
    data[passenger].append(stations)

data_sort = sorted(data.values())

dict_of_means = dict.fromkeys(['1 - 2', '2 - 3', '3 - 4', '4 - 5'], 0)
for stations in data_sort:
    for station in stations:
        if station[0] == 1 and station[1] <= N:
            dict_of_means['1 - 2'] += 1
        elif station[0] == 2 and station[1] <= N:
            dict_of_means['2 - 3'] += 1
        elif station[0] == 3 and station[1] <= N:
            dict_of_means['3 - 4'] += 1
        elif station[0] == 4 and station[1] <= N:
            dict_of_means['4 - 5'] += 1

print(dict_of_means)
dict_of_means_sort = sorted(dict_of_means.items(), key=lambda x: -x[1])
for stations, count in dict_of_means_sort:
    if count != 0:
        print(stations)
print(dict_of_means_sort)
