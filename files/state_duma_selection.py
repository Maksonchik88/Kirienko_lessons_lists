file = open("files/check.txt")
text = file.readlines()

file.close()

data = {}  # {'Party One': [100000], 'Party Two': [200000], 'Party Three': [400000]}
constanta = 450
total_votes = 0  # 700000
for line in text:
    party, number, votes = line.split()
    votes = int(votes)
    party_name = ' '.join([party, number])
    data[party_name] = votes
    total_votes += votes

FIP = total_votes / constanta  # 1555.5555555555557

number_of_seats = {}  # {'Party One': [64, 0.2857142857142918], 'Party Two': [128, 0.5714285714285836], 'Party Three': [257, 0.14285714285716722]}
for party, number in data.items():
    temp = number / FIP
    remainder = (number * constanta) / total_votes
    remainder = remainder - int(remainder)
    number_of_seats[party] = [int(temp)]
    number_of_seats[party].append(remainder)

for party, numbers_list in number_of_seats.items():
    for position in numbers_list:
        passing_score = total_votes / FIP
        if passing_score <= constanta:
            pass