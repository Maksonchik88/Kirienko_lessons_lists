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

max_score = 0
pre_max_score = 0
max_cand = []
pre_max_cand = []
for fullmane, score in data.items():
    if score > max_score:
        pre_max_score = max_score
        max_score = score
        pre_max_cand = max_cand
        max_cand = fullmane
if (100 * max_score)/total_voces > 50:
    print(max_cand)
elif (100 * max_score)/total_voces <= 50:
    print(max_cand, pre_max_cand, sep='\n')
