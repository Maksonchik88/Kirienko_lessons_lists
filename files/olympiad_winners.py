file = open("files/check.txt")
lines = file.readlines()

file.close()

data = {}
number_of_participants = 0
for line in lines:
    line_for_sort = line.split()
    ball = int(line_for_sort[-1])
    name = ' '.join(line_for_sort[: -1])
    number_of_participants += 1
    if name not in data:
        data[name] = ball

max_score = max(data.values())
data_sort = sorted(data.items(), key=lambda x: x[1], reverse=True)
gpa = int((number_of_participants * 45) / 100)

winners = {}
not_winners = {}
for name, score in data_sort:
    if gpa != 0:
        winners[name] = score
        gpa -= 1
    else:
        not_winners[name] = score

winners_sort = sorted(winners.items(), key=lambda x: -x[1])
not_winners_sort = sorted(not_winners.items(), key=lambda x: -x[1])

if winners_sort[-1][1] == not_winners_sort[0][1]:
    temp = winners_sort[-1][1]
    if temp > (max_score/2):
        print(temp)
else:
    print(winners_sort[-1][1])


