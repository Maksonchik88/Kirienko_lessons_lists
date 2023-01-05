file = open("files/check.txt")
N = int(file.readline())
lines = file.readlines()

file.close()

start_station = {}  # {1: 2, 3: 1}
end_station = {}  # {5: 2, 2: 1}
for line in lines:
    _, _, start, end = line.split()
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
for i in range(1, N):
    if i in start_station:
        current_passengers += start_station[i]
        data[i] = current_passengers
        if max_passengers < current_passengers:
            max_passengers = current_passengers
    if i in end_station:
        current_passengers -= end_station[i]
        if current_passengers >= max_passengers:
            data[i] = current_passengers
            max_passengers = current_passengers
    if i not in start_station and i not in end_station:
        data[i] = current_passengers

for station in data.keys():
    print(station,'-',station +1, sep='')