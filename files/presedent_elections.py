file = open("files/check.txt")
candidates = file.readlines()

file.close()

data = {}  # {'Полуэкт Варфоломеев': 2, 'Варфоломей Виссарионов': 3, 'Виссарион Полуэктов': 1}
total_votes = 0  # 6
for candidat in candidates:
    candidat = ' '.join(candidat.split())
    total_votes += 1
    if candidat not in data:
        data[candidat] = 0
    data[candidat] += 1

votes_list = sorted(data.values(), reverse=True)  # [3, 2, 1]

data_rev = {}  # {2: ['Полуэкт Варфоломеев'], 3: ['Варфоломей Виссарионов'], 1: ['Виссарион Полуэктов']}

for fullname, votes in data.items():
    if votes not in data_rev:
        data_rev[votes] = []
    data_rev[votes].append(fullname)

first_place = 0
second_place = 0
for votes, fullname in data_rev.items():
    if first_place < votes:
        second_place = first_place
        first_place = votes
    elif second_place < votes:
        second_place = votes

formula = (100 * first_place / total_votes)

if formula > 50:
    print(*data_rev[first_place])
else:
    print(*data_rev[first_place], *data_rev[second_place], sep='\n')
