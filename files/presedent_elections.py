file = open("files/check.txt")
candidates = file.readlines()

file.close()

data = {}  # {'Полуэкт Варфоломеев': 2, 'Варфоломей Виссарионов': 3, 'Виссарион Полуэктов': 1}
total_voces = 0  # 6
for candidat in candidates:
    candidat = ' '.join(candidat.split())
    total_voces += 1
    if candidat not in data:
        data[candidat] = 0
        data[candidat] += 1
    else:
        data[candidat] += 1

votes_list = sorted(data.values(), reverse=True)  # [3, 2, 1]

data_rev = {}  # {'Варфоломей Виссарионов': 3, 'Полуэкт Варфоломеев': 2, 'Виссарион Полуэктов': 1}


for num in votes_list:
    for fullname, votes in data.items():
        if num == votes:
            data_rev[fullname] = num
data_tuple = list(data_rev.items())  # [('Варфоломей Виссарионов', 3), ('Полуэкт Варфоломеев', 2), ('Виссарион Полуэктов', 1)]


if (100 * data_tuple[0][1])/total_voces > 50:
    print(data_tuple[0][0])
elif (100 * data_tuple[0][1])/total_voces <= 50:
    print(data_tuple[0][0], data_tuple[1][0], sep='\n')
