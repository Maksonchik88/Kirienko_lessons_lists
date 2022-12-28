"""
Вывести номера школ, упорядочив по среднему баллу.
Если средний балл одинаков, то номера школ выводить в порядке возрастания.
"""
# make a new dict
file = open("files/check.txt")
data = {}
for line in file:
    school, score = line.split()[2:]
    school, score = int(school), int(score)
    if school not in data:
        data[school] = [score]
    else:
        data[school].append(score)
file.close()
# count average values
for school, score in data.items():
    middle_score = sum(score)/len(score)
    data[school] = middle_score
# sort scores in descending order
data_reverse = {}
for school, avg_score in data.items():
    if avg_score not in data_reverse:
        data_reverse[avg_score] = [school]
    else:
        data_reverse[avg_score].append(school)

scores_sorted = sorted(data_reverse.keys(), reverse=True)

for score in scores_sorted:
    school_list = data_reverse[score]
    school_list.sort()
    print(*school_list, end=' ')
