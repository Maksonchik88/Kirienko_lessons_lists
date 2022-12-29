file = open("files/check.txt")

data = {}
max_score = 0
for line in file:
    _, _, school, score = line.split()
    school, score = int(school), int(score)
    if score >= max_score:
        max_score = score
    if school not in data:
        data[school] = [score]
    else:
        data[school].append(score)

file.close()

data_count_of_winners = {}
for school, scores in data.items():
    counter = 0
    for score in scores:
        if score == max_score:
            counter += 1
    data_count_of_winners[school] = counter

rev_data_count_of_winners = {}
for school, score in data_count_of_winners.items():
    if score not in rev_data_count_of_winners:
        rev_data_count_of_winners[score] = [school]
    else:
       rev_data_count_of_winners[score].append(school)

max_count = max(rev_data_count_of_winners.keys())

schools_enter = sorted(rev_data_count_of_winners[max_count])
print(*schools_enter)
# max_school = (max(data_count_of_winners, key=data_count_of_winners.get))