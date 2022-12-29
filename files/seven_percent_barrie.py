file = open("files/check.txt")
lines = file.readlines()

file.close()

lines = list((line.rstrip() for line in lines))

parties_list = lines[lines.index("PARTIES:") + 1: lines.index("VOTES:")]
votes_list = lines[lines.index("VOTES:") + 1:]

data_parties_keys = dict.fromkeys(parties_list, 0)

global_votes = 0
for voice in votes_list:
    if voice in data_parties_keys:
        global_votes += 1
        data_parties_keys[voice] += 1
    else:
        continue

for party, votes in data_parties_keys.items():
    if votes >= 7 * global_votes / 100:
        print(party)