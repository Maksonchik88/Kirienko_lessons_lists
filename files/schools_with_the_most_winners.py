file = open("files/check.txt")

data = {}
for line in file:
    _, _, school, score = line.split()
    school, score = int(school), int(score)
    if school not in data:
        data[school] = [score]
    else:
        data[school].append(score)

file.close()

scores_list = list(data.values())

max_score = max(list(map(lambda x: x[0], scores_list)))

data_count_of_winners = {}
for school, scores in data.items():
    counter = 0
    for score in scores:
        if score == max_score:
            counter += 1
    data_count_of_winners[school] = int(counter)

max_school = (max(data_count_of_winners, key=data_count_of_winners.get))

print(max_school)

