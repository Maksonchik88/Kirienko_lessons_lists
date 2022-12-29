file = open("files/check.txt")
raw_text = file.readlines()

file.close()

processed_text = list((line.rstrip() for line in raw_text))
# processed_text = list(filter(None, (line.rstrip() for line in raw_text))
print(processed_text)
parties_list = processed_text[processed_text.index("PARTIES:") + 1: processed_text.index("VOTES:")]
votes_list = processed_text[processed_text.index("VOTES:") + 1:]

data = dict.fromkeys(parties_list, 0)
for voice in votes_list:
    if voice not in data:
        continue
    else:
        data[voice] += 1

revers_data = {}
for party, counter in data.items():
    if counter not in revers_data:
        revers_data[counter] = [party]
    else:
        revers_data[counter].append(party)

count_sort = sorted(revers_data.keys(), reverse=True)

for num in count_sort:
     parties_lst = revers_data[num]
     parties_lst.sort()
     for party in parties_lst:
         print(party)