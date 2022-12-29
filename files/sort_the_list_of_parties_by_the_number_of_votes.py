file = open("files/check.txt")
raw_text = file.readlines()

file.close()

processed_text = list(filter(None, (line.rstrip() for line in raw_text)))
print(processed_text)
parties_list = processed_text[processed_text.index("PARTIES:") + 1: processed_text.index("VOTES:")]
votes_list = processed_text[processed_text.index("VOTES:") + 1:]
print(parties_list)
print(votes_list)
data = dict.fromkeys(parties_list, 0)
print(data)
for voice in votes_list:
    data[voice] += 1
print(data)
revers_data = {}
for party, counter in data.items():
    if counter not in revers_data:
        revers_data[counter] = [party]
    else:
        revers_data[counter].append(party)
print(revers_data)
count_sort = sorted(revers_data.keys(), reverse=True)
print(count_sort)
for num in count_sort:
    a = revers_data[num]
    a.sort()
    print(*a)