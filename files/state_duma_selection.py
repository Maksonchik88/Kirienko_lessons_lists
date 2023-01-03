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
total = 0  # 449
number_of_seats = {}  # {'Party One': 64, 'Party Two': 128, 'Party Three': 257}
fractional_dictionary = {}  # {'Party One': 0.2857142857142918, 'Party Two': 0.5714285714285836, 'Party Three': 0.14285714285716722}
for party, number in data.items():
    temp = number / FIP
    remainder = (number * constanta) / total_votes
    remainder = remainder - int(remainder)
    total += int(temp)
    number_of_seats[party] = int(temp)
    fractional_dictionary[party] = remainder
sort_fract_dict = sorted(fractional_dictionary.items(), key=lambda x: -x[1])  # [('Party Two', 0.5714285714285836), ('Party One', 0.2857142857142918), ('Party Three', 0.14285714285716722)]
sort_num_of_seats = sorted(number_of_seats.items(), key=lambda x: -x[1])  # [('Party Three', 257), ('Party Two', 128), ('Party One', 64)]

i = 0
extra_scores = constanta - total
while extra_scores != 0:
    for a, b in sort_fract_dict:
        number_of_seats[a] += 1
        i += 1
    extra_scores -= 1
print(number_of_seats)
