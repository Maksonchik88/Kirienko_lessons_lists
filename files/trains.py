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
temp = 0
for i in range(N + 1):
    i += 1
    if i in start_station:
        if i not in end_station:
            temp += start_station[i]
            data[i] = temp
        if i in end_station:
            temp = start_station[i] - end_station[i]
            data[i] = temp
    elif i not in start_station:
        if i in end_station:
            pass
