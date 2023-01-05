file = open("files/check.txt")
N = int(file.readline())
lines = file.readlines()

file.close()

start_station = {}  # {1: 2, 3: 1}
end_station = {}  # {5: 2, 2: 1}
for line in lines:
    start, end = line.split()[-2:]
    start, end = int(start), int(end)
    if start not in start_station:
        start_station[start] = 0
    start_station[start] += 1
    if end not in end_station:
        end_station[end] = 0
    end_station[end] += 1

data = {}
current_passengers = 0
max_passengers = 0
for station in range(1, N):
    if station in start_station:
        current_passengers += start_station[station]
    if station in end_station:
        current_passengers -= end_station[station]
    data[station] = current_passengers
    if current_passengers >= max_passengers:
        max_passengers = current_passengers

for station, count in data.items():
    if count == max_passengers:
        print(station, '-', station + 1, sep='')
