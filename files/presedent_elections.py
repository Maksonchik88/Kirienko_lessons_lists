file = open("files/check.txt")
candidates = file.readlines()

file.close()

data = {}
total_voces = 0
for candidat in candidates:
    candidat = ' '.join(candidat.split())
    total_voces += 1
    if candidat not in data:
        data[candidat] = 0
        data[candidat] += 1
    else:
        data[candidat] += 1

data_tuple = sorted(data.items(), key=lambda x: x[1], reverse=True)

if (100 * data_tuple[0][1])/total_voces > 50:
    print(data_tuple[0][0])
elif (100 * data_tuple[0][1])/total_voces <= 50:
    print(data_tuple[0][0], data_tuple[1][0], sep='\n')
