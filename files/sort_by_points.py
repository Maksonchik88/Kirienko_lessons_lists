file = open("files/check.txt")

data = {}
for line in file:
    surname, name, _, score = line.split()
    score = int(score)
    fullname = ' '.join([surname, name])
    if score not in data:
        data[score] = [fullname]
    else:
        data[score].append(fullname)

file.close()

sorted_by_scores = sorted(data.keys(), reverse=True)
for score in sorted_by_scores:
    for surname in data[score]:
        print(surname, score)
