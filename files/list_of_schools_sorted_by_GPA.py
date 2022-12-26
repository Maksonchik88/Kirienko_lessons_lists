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
scores_sorted = sorted(data.values(), reverse=True)
schools_sorted = sorted(data.keys())

data_reverse = {score: school for school, score in data.items()}
print(data)
print(data_reverse)
# find and print schools according to the task statement
for score_1 in scores_sorted:
    for school_1 in schools_sorted:














